"""
GODMODE V9 — Auto-Ingestor
Automatically rips new models from OpenRouter, applies strict filters to block spam,
and uses Groq AI to autonomously construct their JSON schema before appending them to the registry.
"""
from __future__ import annotations

import json
import logging
import time
from pathlib import Path

import requests

from src.core.groq_client import GroqEngine

logger = logging.getLogger(__name__)

MODELS_JSON_PATH = Path("data/models.json")
OPENROUTER_URL = "https://openrouter.ai/api/v1/models"
REQUEST_TIMEOUT = 30
MAX_INGEST_PER_RUN = 175

# Strict Spam Filter
BANNED_TAGS = {"nsfw", "roleplay", "uncensored", "waifu", "rp", "erp", "my-little-pony"}
ALLOWED_PROVIDERS = {
    "openai", "anthropic", "meta", "google", "mistral", "cohere", "groq", 
    "deepseek", "qwen", "liquid", "databricks", "01-ai", "perplexity"
}

def _load_registry() -> dict:
    try:
        return json.loads(MODELS_JSON_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        logger.error(f"Cannot load registry: {e}")
        return {"models": []}

def _atomic_write(data: dict) -> None:
    tmp = MODELS_JSON_PATH.with_suffix(".tmp")
    try:
        content = json.dumps(data, indent=2, ensure_ascii=False)
        json.loads(content)  # Val
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(MODELS_JSON_PATH)
    except Exception as e:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"Atomic write failed: {e}")

def _fetch_openrouter() -> list[dict]:
    try:
        resp = requests.get(OPENROUTER_URL, timeout=REQUEST_TIMEOUT, headers={"User-Agent": "LLMCosts-Ingestor"})
        resp.raise_for_status()
        return resp.json().get("data", [])
    except Exception as e:
        logger.warning(f"OpenRouter fetch failed: {e}")
        return []

def _is_spam(model: dict) -> bool:
    mid = model.get("id", "").lower()
    name = model.get("name", "").lower()
    desc = model.get("description", "").lower()

    for banned in BANNED_TAGS:
        if banned in mid or banned in name or banned in desc:
            return True

    provider = mid.split("/")[0] if "/" in mid else "unknown"
    if provider not in ALLOWED_PROVIDERS:
        # If it's a random user upload, we might want to skip it to ensure high quality
        return True

    return False

def _generate_ai_schema(groq: GroqEngine, mid: str, name: str, desc: str) -> dict:
    prompt = (
        "You are an AI database classification system.\n"
        f"Analyze the LLM '{name}' (ID: {mid}).\n"
        f"Description: {desc}\n\n"
        "Return a strictly valid JSON object with the following keys:\n"
        "- tier: one of ['budget', 'standard', 'mid', 'premium']\n"
        "- capabilities: array of strings (e.g. ['text', 'vision', 'coding'])\n"
        "- use_cases: array of strings (top 3 best use cases)\n"
        "- not_good_for: array of strings (top 2 weaknesses)\n"
        "- tags: array of strings (e.g. ['frontier', 'fast', 'open-source'])\n"
        "Do not wrap in markdown blocks, output raw JSON only."
    )
    res = groq.generate("OUTPUT PURE JSON.", prompt, max_tokens=300, response_format={"type": "json_object"})
    try:
        if res:
            return json.loads(res.strip())
    except Exception as e:
        logger.warning(f"Groq API hallucinated JSON for {mid}: {e}")
    return {}

def run_ingestion() -> dict:
    summary = {"ingested": 0, "skipped_spam": 0, "errors": 0}
    registry = _load_registry()
    models = registry.get("models", [])
    existing_ids = {m["id"] for m in models if m.get("id")}

    live_models = _fetch_openrouter()
    if not live_models:
        return summary

    try:
        groq = GroqEngine()
    except Exception as e:
        logger.error(f"Groq unavailable for ingestion: {e}")
        return summary

    added = 0
    for lm in live_models:
        mid = lm.get("id")
        if not mid or mid in existing_ids:
            continue

        if _is_spam(lm):
            summary["skipped_spam"] += 1
            continue

        if added >= MAX_INGEST_PER_RUN or groq.all_keys_exhausted():
            logger.info("Reached MAX_INGEST_PER_RUN or exhausted keys.")
            break

        logger.info(f"Ingesting new model: {mid}")
        try:
            name = lm.get("name") or mid
            desc = lm.get("description") or ""

            # AI Generation — safe, never crashes
            ai_data = _generate_ai_schema(groq, mid, name, desc)

            # Math Enforcement — clamp all prices to >= 0
            pricing = lm.get("pricing") or {}
            inp = max(0.0, float(pricing.get("prompt") or 0)) * 1_000_000
            out = max(0.0, float(pricing.get("completion") or 0)) * 1_000_000
            try:
                ctx_win = int(lm["context_length"]) if lm.get("context_length") else None
            except (ValueError, TypeError):
                ctx_win = None

            new_entry = {
                "id": mid,
                "name": name,
                "slug": mid.replace("/", "-"),
                "provider": mid.split("/")[0] if "/" in mid else "unknown",
                "provider_name": mid.split("/")[0].title() if "/" in mid else "Unknown",
                "version": "",
                "release_date": time.strftime("%Y-%m-%d", time.gmtime()),
                "pricing": {
                    "input_per_1m": round(inp, 6),
                    "output_per_1m": round(out, 6),
                    "cached_input_per_1m": None,
                    "batch_input_per_1m": None,
                    "batch_output_per_1m": None,
                    "currency": "USD",
                    "pricing_model": "per_token"
                },
                "context_window": ctx_win,
                "max_output_tokens": None,
                "knowledge_cutoff": "Unknown",
                "capabilities": ai_data.get("capabilities") or ["text"],
                "benchmarks": {
                    "arena_elo": None,
                    "arena_elo_source": None
                },
                "performance": {
                    "speed_tokens_per_sec": None,
                    "median_latency_ms": None
                },
                "use_cases": ai_data.get("use_cases") or ["general_purpose"],
                "not_good_for": ai_data.get("not_good_for") or [],
                "competing_models": [],
                "price_stability": "unknown",
                "price_trend": "stable",
                "links": {
                    "affiliate_link": "https://openrouter.ai/?ref=llmcosts"
                },
                "last_verified": time.strftime("%Y-%m-%d", time.gmtime()),
                "last_verified_status": "confirmed",
                "verified_by": "automated_ingestor",
                "data_confidence": "medium",
                "field_confidence": {
                    "pricing": 100,
                    "benchmarks": 0,
                    "performance": 0,
                    "use_cases": 60
                },
                "tags": ai_data.get("tags") or [],
                "tier": ai_data.get("tier") or "standard",
                "open_source": False,
                "self_hostable": False
            }

            registry["models"].append(new_entry)
            existing_ids.add(mid)  # prevent re-processing in same run
            added += 1
            summary["ingested"] += 1
            time.sleep(2.5)  # Throttle Groq API

        except Exception as model_err:
            logger.error(f"Failed to ingest model {mid}: {model_err}", exc_info=True)
            summary["errors"] += 1
            continue

    if added > 0:
        registry["total_models"] = len(registry["models"])
        registry["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        _atomic_write(registry)
        logger.info(f"Successfully ingested {added} new models.")

    return summary

if __name__ == "__main__":
    run_ingestion()
