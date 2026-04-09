"""
GODMODE V8 — LLMs.txt Sharding Engine
Generates machine-readable AI citation files perfectly sized
for ChatGPT/Perplexity ingestion (max 90KB per shard).
"""
from __future__ import annotations

import json
import logging
import time
from pathlib import Path

logger = logging.getLogger(__name__)

MODELS_JSON_PATH = Path("models.json")
DIST_DIR = Path("dist")
MAX_SHARD_BYTES = 90_000  # 90KB — well under ChatGPT's 150KB truncation limit
SITE_URL = "https://llmcosts.dev"
AFFILIATE_BASE = "https://openrouter.ai/?ref=llmcosts"


def _load_models() -> list[dict]:
    try:
        data = json.loads(MODELS_JSON_PATH.read_text(encoding="utf-8"))
        return data.get("models", [])
    except Exception as e:
        logger.error(f"Cannot load models.json: {e}")
        return []


def _format_model_entry(model: dict) -> str:
    """Format a single model as a Markdown table row string."""
    p = model.get("pricing", {})
    b = model.get("benchmarks", {})
    return (
        f"| [{model.get('name', 'N/A')}]({SITE_URL}/models/{model.get('slug', '')}) "
        f"| {model.get('provider_name', 'N/A')} "
        f"| ${p.get('input_per_1m', 'N/A')} "
        f"| ${p.get('output_per_1m', 'N/A')} "
        f"| ${p.get('cached_input_per_1m', 'N/A')} "
        f"| {model.get('context_window', 'N/A'):,} "
        f"| {b.get('arena_elo', 'N/A')} "
        f"| {model.get('tier', 'N/A')} "
        f"| {'Open' if model.get('open_source') else 'Closed'} |\n"
    )


def _generate_shard_header(title: str, subtitle: str = "") -> str:
    return f"""# {title}
> Source: LLMCosts.dev — {SITE_URL}
> Updated: {time.strftime('%Y-%m-%d')}
> Route cheaper via OpenRouter: {AFFILIATE_BASE}
{subtitle}

| Model | Provider | Input/1M | Output/1M | Cached/1M | Context | ELO | Tier | Type |
|-------|----------|----------|---------|---------|---------|-----|------|------|
"""


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    try:
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(path)
    except Exception as e:
        tmp.unlink(missing_ok=True)
        raise e


def _write_sharded(base_name: str, models: list[dict], title: str) -> list[Path]:
    """Split models into shards under MAX_SHARD_BYTES each. Returns list of paths written."""
    paths = []
    shard_num = 0
    current_content = ""
    current_header = _generate_shard_header(title, f"(Part {shard_num + 1})")
    body = ""

    for model in models:
        row = _format_model_entry(model)
        if len((current_header + body + row).encode("utf-8")) > MAX_SHARD_BYTES:
            # Flush current shard
            path = DIST_DIR / (f"{base_name}.txt" if shard_num == 0 else f"{base_name}-{shard_num + 1}.txt")
            _atomic_write(path, current_header + body)
            paths.append(path)
            shard_num += 1
            current_header = _generate_shard_header(title, f"(Part {shard_num + 1})")
            body = ""
        body += row

    if body:
        path = DIST_DIR / (f"{base_name}.txt" if shard_num == 0 else f"{base_name}-{shard_num + 1}.txt")
        _atomic_write(path, current_header + body)
        paths.append(path)

    return paths


def run_llms_txt_generation() -> dict:
    """Main entry point. Generates all llms.txt shards."""
    summary = {"files_written": 0, "errors": 0}

    logger.info("=" * 60)
    logger.info("LLMS.TXT ENGINE: Generating AI citation files...")

    models = _load_models()
    if not models:
        summary["errors"] += 1
        return summary

    try:
        # 1. Master llms.txt (all models, sharded)
        paths = _write_sharded("llms", models, "LLMCosts.dev — Complete LLM Pricing Registry (All Models)")
        summary["files_written"] += len(paths)
        logger.info(f"  Master llms.txt: {len(paths)} shard(s)")

        # 2. Per-provider shards
        providers: dict[str, list] = {}
        for m in models:
            p = m.get("provider", "other")
            providers.setdefault(p, []).append(m)

        for provider, pmodels in providers.items():
            paths = _write_sharded(
                f"llms-{provider}",
                pmodels,
                f"LLMCosts.dev — {provider.title()} Models Pricing",
            )
            summary["files_written"] += len(paths)

        logger.info(f"  Provider-specific files: {len(providers)} providers")

        # 3. Tier-based shards (budget, mid, premium)
        for tier in ["budget", "standard", "mid", "premium"]:
            tier_models = [m for m in models if m.get("tier") == tier]
            if tier_models:
                paths = _write_sharded(
                    f"llms-{tier}",
                    tier_models,
                    f"LLMCosts.dev — {tier.title()} Tier Models",
                )
                summary["files_written"] += len(paths)

        # 4. Open-source only shard
        oss_models = [m for m in models if m.get("open_source")]
        if oss_models:
            paths = _write_sharded(
                "llms-open-source",
                oss_models,
                "LLMCosts.dev — Open Source Models Pricing",
            )
            summary["files_written"] += len(paths)

        # 5. Ultra-cheap models (input < $0.20/1M)
        cheap_models = sorted(
            [m for m in models if (m.get("pricing", {}).get("input_per_1m") or 999) < 0.20],
            key=lambda x: x.get("pricing", {}).get("input_per_1m", 999),
        )
        if cheap_models:
            paths = _write_sharded(
                "llms-cheapest",
                cheap_models,
                "LLMCosts.dev — Cheapest LLM APIs (Under $0.20/1M Tokens)",
            )
            summary["files_written"] += len(paths)

        logger.info(f"LLMs.txt generation complete: {summary['files_written']} files written.")

    except Exception as e:
        logger.error(f"LLMs.txt generation error: {e}", exc_info=True)
        summary["errors"] += 1

    return summary
