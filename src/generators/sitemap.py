"""
GODMODE V8 — Sitemap Builder + Google Indexing API
Generates sitemap.xml and pings Google Indexing API
for every new/updated URL (max 200/day drip-feed).
"""
from __future__ import annotations

import json
import logging
import os
import time
import xml.sax.saxutils as saxutils
from pathlib import Path
from typing import Optional

import requests

logger = logging.getLogger(__name__)

MODELS_JSON_PATH = Path("data/models.json")
DIST_DIR = Path("dist")
SITE_URL = os.getenv("SITE_URL", "https://llmcosts.dev")
GOOGLE_INDEXING_API_URL = "https://indexing.googleapis.com/v3/urlNotifications:publish"
GOOGLE_API_KEY = os.getenv("GOOGLE_INDEXING_API_KEY", "")
MAX_GOOGLE_PINGS_PER_DAY = 200
INDEXING_STATE_PATH = Path("data/indexing_state.json")


def _load_models() -> list[dict]:
    try:
        data = json.loads(MODELS_JSON_PATH.read_text(encoding="utf-8"))
        return data.get("models", [])
    except Exception as e:
        logger.error(f"Cannot load models.json: {e}")
        return []


def _load_indexing_state() -> dict:
    try:
        if INDEXING_STATE_PATH.exists():
            return json.loads(INDEXING_STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        pass
    return {"pinged_urls": [], "last_reset": ""}


def _save_indexing_state(state: dict) -> None:
    try:
        tmp = INDEXING_STATE_PATH.with_suffix(".tmp")
        tmp.write_text(json.dumps(state, indent=2), encoding="utf-8")
        tmp.replace(INDEXING_STATE_PATH)
    except Exception as e:
        logger.warning(f"Could not save indexing state: {e}")


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    try:
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(path)
    except Exception as e:
        tmp.unlink(missing_ok=True)
        raise e


def _ping_google(url: str, api_key: str) -> bool:
    """Returns True on success. Never raises."""
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        payload = {"url": url, "type": "URL_UPDATED"}
        resp = requests.post(
            GOOGLE_INDEXING_API_URL,
            headers=headers,
            json=payload,
            timeout=15,
        )
        if resp.status_code == 200:
            return True
        logger.warning(f"Google Indexing API returned {resp.status_code} for {url}")
        return False
    except Exception as e:
        logger.warning(f"Google Indexing API error for {url}: {e}")
        return False


def _generate_all_urls(models: list[dict]) -> list[dict]:
    """Returns list of all site URLs with priority and changefreq."""
    urls = [
        {"loc": SITE_URL, "priority": "1.0", "changefreq": "daily"},
        {"loc": f"{SITE_URL}/compare", "priority": "0.9", "changefreq": "daily"},
        {"loc": f"{SITE_URL}/configs", "priority": "0.8", "changefreq": "daily"},
        {"loc": f"{SITE_URL}/daily-report", "priority": "0.9", "changefreq": "daily"},
    ]

    for m in models:
        mid = m.get("id")
        if not mid:
            continue  # skip malformed entries
        slug = m.get("slug") or mid.replace("/", "-")
        urls.append({
            "loc": f"{SITE_URL}/models/{slug}",
            "priority": "0.8",
            "changefreq": "daily",
        })

    # Add VS Pages from Checkpoint
    try:
        vs_state = json.loads(Path("data/vs_checkpoint.json").read_text(encoding="utf-8"))
        for vs_slug in vs_state.get("completed", []):
            urls.append({
                "loc": f"{SITE_URL}/compare/{vs_slug}",
                "priority": "0.8",
                "changefreq": "weekly",
            })
    except Exception:
        pass

    return urls


def _build_sitemap_xml(urls: list[dict]) -> str:
    today = time.strftime("%Y-%m-%d")
    entries = ""
    for u in urls:
        # XML-escape the URL to prevent malformed XML on special chars
        safe_loc = saxutils.escape(u["loc"])
        entries += f"""  <url>
    <loc>{safe_loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{u['changefreq']}</changefreq>
    <priority>{u['priority']}</priority>
  </url>
"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}</urlset>"""


def run_sitemap_generation() -> dict:
    """Main entry point. Builds sitemap and pings Google Indexing API."""
    summary = {"urls_in_sitemap": 0, "google_pings_sent": 0, "errors": 0}

    logger.info("=" * 60)
    logger.info("SITEMAP BUILDER: Generating sitemap.xml...")

    models = _load_models()
    urls = _generate_all_urls(models)
    summary["urls_in_sitemap"] = len(urls)

    try:
        sitemap_xml = _build_sitemap_xml(urls)
        _atomic_write(DIST_DIR / "sitemap.xml", sitemap_xml)
        logger.info(f"  ✅ sitemap.xml with {len(urls)} URLs")
    except Exception as e:
        logger.error(f"Sitemap write failed: {e}")
        summary["errors"] += 1
        return summary

    # Google Indexing API: drip-feed max 200 new URLs per day
    if not GOOGLE_API_KEY:
        logger.info("No GOOGLE_INDEXING_API_KEY set. Skipping Google pings.")
        return summary

    state = _load_indexing_state()
    today = time.strftime("%Y-%m-%d")
    if state.get("last_reset") != today:
        state["pinged_urls"] = []
        state["last_reset"] = today

    pinged_set = set(state.get("pinged_urls", []))
    pings_sent = 0

    for url_data in urls:
        if pings_sent >= MAX_GOOGLE_PINGS_PER_DAY:
            logger.info(f"Daily Google ping limit ({MAX_GOOGLE_PINGS_PER_DAY}) reached.")
            break
        url = url_data["loc"]
        if url in pinged_set:
            continue
        success = _ping_google(url, GOOGLE_API_KEY)
        if success:
            pinged_set.add(url)
            pings_sent += 1
            logger.info(f"  🔔 Google pinged: {url}")
            time.sleep(0.1)  # Respect rate limits

    state["pinged_urls"] = list(pinged_set)
    _save_indexing_state(state)
    summary["google_pings_sent"] = pings_sent
    logger.info(f"Sitemap complete: {summary}")
    return summary
