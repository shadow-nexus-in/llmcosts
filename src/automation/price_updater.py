"""
GODMODE V8 — Price Updater
Fetches live pricing from two independent sources, cross-validates,
and performs atomic writes to models.json.
"""
from __future__ import annotations

import html
import json
import logging
import re
import time
from pathlib import Path
from typing import Optional

import requests

logger = logging.getLogger(__name__)

MODELS_JSON_PATH = Path("data/models.json")
OPENROUTER_PRICES_URL = "https://openrouter.ai/api/v1/models"
LITELLM_PRICES_URL = (
    "https://raw.githubusercontent.com/BerriAI/litellm/main/"
    "model_prices_and_context_window.json"
)
CROSS_CHECK_TOLERANCE = 0.10   # 10% tolerance before flagging as unverified
REQUEST_TIMEOUT = 30
MODEL_ID_REGEX = re.compile(r"^[a-zA-Z0-9\-_./]+$")  # XSS prevention


def _safe_get(d: dict, *keys, default=None):
    """Fuzzy key cascade — handles schema changes from providers."""
    synonyms_map = {
        "input": ["input_cost_per_token", "prompt_price", "input_price_per_token",
                  "input", "cost_per_input_token"],
        "output": ["output_cost_per_token", "completion_price", "output_price_per_token",
                   "output", "cost_per_output_token"],
        "context": ["max_tokens", "context_length", "max_context_window", "context_window"],
    }
    for key in keys:
        if key in d:
            return d[key]
        for alt in synonyms_map.get(key, []):
            if alt in d:
                return d[alt]
    return default


def _fetch_openrouter_prices() -> dict[str, dict]:
    """Returns {provider/model: {input_per_1m, output_per_1m}} from OpenRouter."""
    prices: dict[str, dict] = {}
    try:
        resp = requests.get(OPENROUTER_PRICES_URL, timeout=REQUEST_TIMEOUT,
                            headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        for item in resp.json().get("data", []):
            mid = html.escape(str(item.get("id", "")))
            if not MODEL_ID_REGEX.match(mid):
                continue
            try:
                pricing = item.get("pricing", {})
                inp_raw = float(_safe_get(pricing, "prompt", "input", default=0) or 0)
                out_raw = float(_safe_get(pricing, "completion", "output", default=0) or 0)
                # OpenRouter returns per-token; convert to per-1M
                prices[mid] = {
                    "input_per_1m": max(0.0, round(inp_raw * 1_000_000, 6)),
                    "output_per_1m": max(0.0, round(out_raw * 1_000_000, 6)),
                }
            except (ValueError, TypeError):
                continue
    except Exception as e:
        logger.warning(f"OpenRouter fetch failed: {e}")
    logger.info(f"OpenRouter: fetched {len(prices)} model prices.")
    return prices


def _fetch_litellm_prices() -> dict[str, dict]:
    """Returns {provider/model: {input_per_1m, output_per_1m}} from LiteLLM."""
    prices: dict[str, dict] = {}
    try:
        resp = requests.get(LITELLM_PRICES_URL, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        raw: dict = resp.json()
        for mid, info in raw.items():
            mid = html.escape(str(mid))
            if not MODEL_ID_REGEX.match(mid):
                continue
            try:
                inp_tok = float(_safe_get(info, "input", default=0) or 0)
                out_tok = float(_safe_get(info, "output", default=0) or 0)
                prices[mid] = {
                    "input_per_1m": max(0.0, round(inp_tok * 1_000_000, 6)),
                    "output_per_1m": max(0.0, round(out_tok * 1_000_000, 6)),
                }
            except (ValueError, TypeError):
                continue
    except Exception as e:
        logger.warning(f"LiteLLM fetch failed: {e}")
    logger.info(f"LiteLLM: fetched {len(prices)} model prices.")
    return prices


def _cross_check(price_a: float, price_b: float) -> bool:
    """Returns True if both prices agree within tolerance."""
    if price_a <= 0 or price_b <= 0:
        return False
    diff = abs(price_a - price_b) / max(price_a, price_b)
    return diff <= CROSS_CHECK_TOLERANCE


def _detect_new_models(
    or_prices: dict[str, dict],
    ll_prices: dict[str, dict],
    existing_ids: set[str],
) -> list[str]:
    """Returns model IDs that appear in live feeds but NOT in our registry."""
    live_ids = set(or_prices.keys()) | set(ll_prices.keys())
    new_ids = live_ids - existing_ids
    if new_ids:
        logger.info(f"Detected {len(new_ids)} new model(s) in live feeds:")
        for mid in sorted(new_ids):
            logger.info(f"  NEW: {mid}")
    return sorted(new_ids)


def _atomic_write_json(path: Path, data: dict) -> None:
    """Write JSON atomically — temp file, validate, replace."""
    tmp = path.with_suffix(".tmp")
    try:
        content = json.dumps(data, indent=2, ensure_ascii=False)
        json.loads(content)  # Validate before writing
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(path)
        logger.info(f"Atomic write successful: {path}")
    except Exception as e:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"Atomic write failed for {path}: {e}") from e


def run_price_update() -> dict:
    """
    Main entry point. Fetches, cross-checks, and updates models.json.
    Returns summary dict with counts.
    """
    summary = {"updated": 0, "unchanged": 0, "unverified": 0, "new_detected": 0, "errors": 0}

    logger.info("=" * 60)
    logger.info("PRICE UPDATER: Starting live price fetch...")

    # 1. Load current registry
    try:
        registry = json.loads(MODELS_JSON_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        logger.error(f"Cannot load models.json: {e}")
        summary["errors"] += 1
        return summary

    models = registry.get("models", [])
    existing_ids = {m["id"] for m in models if m.get("id")}

    # 2. Fetch from both sources
    or_prices = _fetch_openrouter_prices()
    ll_prices = _fetch_litellm_prices()

    # 3. Detect new models
    new_model_ids = _detect_new_models(or_prices, ll_prices, existing_ids)
    summary["new_detected"] = len(new_model_ids)

    # 4. Update existing model prices
    changed = False
    for model in models:
        mid = model.get("id")
        if not mid:
            continue
        or_data = or_prices.get(mid) or {}
        ll_data = ll_prices.get(mid) or {}

        # Accept input price if cross-check passes
        or_inp = or_data.get("input_per_1m", 0)
        ll_inp = ll_data.get("input_per_1m", 0)
        or_out = or_data.get("output_per_1m", 0)
        ll_out = ll_data.get("output_per_1m", 0)

        if or_inp > 0 and ll_inp > 0 and _cross_check(or_inp, ll_inp):
            new_inp = round((or_inp + ll_inp) / 2, 6)  # Average of two sources
            new_out = round((or_out + ll_out) / 2, 6) if _cross_check(or_out, ll_out) else or_out
            old_inp = model["pricing"].get("input_per_1m", 0)

            if abs(new_inp - old_inp) > 0.0001:  # Price changed
                model["pricing"]["input_per_1m"] = new_inp
                model["pricing"]["output_per_1m"] = new_out
                # Recalculate cost examples
                avg = (new_inp * 0.5 + new_out * 0.5) / 1000
                model["cost_examples"] = {
                    "1k_calls_avg_500_tokens": round(avg * 1000, 4),
                    "10k_calls_avg_500_tokens": round(avg * 10000, 4),
                    "100k_calls_avg_500_tokens": round(avg * 100000, 4),
                    "1m_calls_avg_500_tokens": round(avg * 1000000, 4),
                }
                model["last_verified"] = time.strftime("%Y-%m-%d", time.gmtime())
                model["last_verified_status"] = "confirmed"
                model["verified_by"] = "automated_dual_source"
                # Append price history
                model.setdefault("price_history", []).append({
                    "date": time.strftime("%Y-%m-%d", time.gmtime()),
                    "input_per_1m": new_inp,
                    "output_per_1m": new_out,
                    "note": "Automated dual-source update",
                })
                summary["updated"] += 1
                changed = True
                logger.info(f"  UPDATED: {mid} -> ${new_inp}/${new_out} per 1M")
            else:
                summary["unchanged"] += 1
        elif or_inp > 0:
            # Only one source — mark as unverified but don't update pricing
            model["data_confidence"] = "medium"
            summary["unverified"] += 1
        else:
            summary["unchanged"] += 1

    # 5. Save if anything changed
    if changed:
        registry["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        _atomic_write_json(MODELS_JSON_PATH, registry)

    logger.info(f"Price update complete: {summary}")
    return summary
