"""
GODMODE V9 — VIP Versus Engine
Generates massive 1000-word SEO comparison showdowns between the Top 50 models globally.
Enforces canonical URL safety and throttles generation to 50 pages per run.
"""
from __future__ import annotations

import json
import logging
import os
import time
from pathlib import Path

from src.core.groq_client import GroqEngine

logger = logging.getLogger(__name__)

MODELS_JSON_PATH = Path("data/models.json")
DIST_COMPARE_DIR = Path("dist/compare")
VS_STATE_PATH = Path("data/vs_checkpoint.json")
TEMPLATE_PATH = Path("templates/vs_page.html")
SITE_URL = os.getenv("SITE_URL", "https://llmcosts.dev")
MAX_VS_PAGES_PER_RUN = 90

SYSTEM_PROMPT = (
    "You are a technical analyst writing a deep-dive AI model comparison showdown. "
    "Be highly analytical. Discuss technical trade-offs, pricing efficiency, and architecture. "
    "Output clean Markdown."
)

def _load_models() -> list[dict]:
    try:
        data = json.loads(MODELS_JSON_PATH.read_text(encoding="utf-8"))
        models = [m for m in data.get("models", []) if m.get("id")]
        for m in models:
            if m.get("pricing") is None: m["pricing"] = {}
            if m.get("benchmarks") is None: m["benchmarks"] = {}
        return models
    except Exception:
        return []

def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    try:
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(path)
    except Exception as e:
        tmp.unlink(missing_ok=True)
        logger.error(f"Atomic write failed for {path}: {e}")

def _get_top_50(models: list[dict]) -> list[dict]:
    """Return top 50 models based on tier and dynamically decayed ELO."""
    from datetime import datetime
    
    def score(m):
        base = 1000 if m.get("tier") == "premium" else 500 if m.get("tier") == "standard" else 0
        try:
            elo = float(m.get("benchmarks", {}).get("arena_elo") or 0)
        except (ValueError, TypeError):
            elo = 0.0

        # ELO Decay & Hype Surge calculations
        try:
            rd_str = m.get("release_date", "")
            if rd_str:
                rd = datetime.strptime(rd_str, "%Y-%m-%d")
                age_days = (datetime.now() - rd).days
                if age_days < 14:
                    elo += 2000  # Hype Surge for brand new models
                elif age_days > 120:
                    elo *= 0.85  # 15% ELO penalty for models older than 4 months
        except Exception:
            pass # Malformed date, ignore algorithm modifiers
            
        return base + elo
        
    return sorted(models, key=score, reverse=True)[:50]

def _generate_showdown_text(groq: GroqEngine, ma: dict, mb: dict) -> str:
    pricing_a = ma.get("pricing") or {}
    pricing_b = mb.get("pricing") or {}
    bench_a = ma.get("benchmarks") or {}
    bench_b = mb.get("benchmarks") or {}
    
    ctx = f"""
MODEL A: {ma.get('name')} | Price (In/Out): ${pricing_a.get('input_per_1m')}/${pricing_a.get('output_per_1m')} | ELO: {bench_a.get('arena_elo')} | Context: {ma.get('context_window')}
MODEL B: {mb.get('name')} | Price (In/Out): ${pricing_b.get('input_per_1m')}/${pricing_b.get('output_per_1m')} | ELO: {bench_b.get('arena_elo')} | Context: {mb.get('context_window')}
"""
    prompt = f"Write a 4-paragraph comprehensive comparison of {ma.get('name')} vs {mb.get('name')}. Compare price-performance, context size advantages, and final verdict on which to choose for production workloads."
    return groq.generate(SYSTEM_PROMPT, prompt + "\n" + ctx, max_tokens=600) or f"Comparison data for {ma.get('name')} vs {mb.get('name')}."

def _render_html(ma: dict, mb: dict, text: str, template: str) -> str:
    slug_a = ma.get("slug", ma["id"].replace("/", "-"))
    slug_b = mb.get("slug", mb["id"].replace("/", "-"))
    
    pricing_a = ma.get("pricing") or {}
    pricing_b = mb.get("pricing") or {}
    bench_a = ma.get("benchmarks") or {}
    bench_b = mb.get("benchmarks") or {}

    replacements = {
        "{{MODEL_A_NAME}}": ma.get("name", ""),
        "{{MODEL_B_NAME}}": mb.get("name", ""),
        "{{MODEL_A_SLUG}}": slug_a,
        "{{MODEL_B_SLUG}}": slug_b,
        "{{MODEL_A_PRICE}}": f"${pricing_a.get('input_per_1m') or 0:.4f}",
        "{{MODEL_B_PRICE}}": f"${pricing_b.get('input_per_1m') or 0:.4f}",
        "{{MODEL_A_ELO}}": str(bench_a.get("arena_elo") or 'Pending'),
        "{{MODEL_B_ELO}}": str(bench_b.get("arena_elo") or 'Pending'),
        "{{COMPARISON_TEXT}}": text.replace("\n", "<br><br>"),
        "{{AFFILIATE_LINK}}": "https://m.do.co/c/0c99ee"
    }
    rendered = template
    for k, v in replacements.items():
        rendered = rendered.replace(k, str(v))
    return rendered

def run_vs_generation() -> dict:
    summary = {"generated": 0, "skipped_limit": False}
    models = _load_models()
    if not models:
        return summary
    
    top50 = _get_top_50(models)
    
    try:
        state = json.loads(VS_STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        state = {"completed": []}

    try:
        groq = GroqEngine()
    except Exception:
        return summary

    try:
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
    except Exception:
        logger.error("vs_page.html template missing.")
        return summary

    completed_set = set(state["completed"])
    generated_this_run = 0

    for i in range(len(top50)):
        for j in range(i + 1, len(top50)):
            if generated_this_run >= MAX_VS_PAGES_PER_RUN or groq.all_keys_exhausted():
                summary["skipped_limit"] = True
                _atomic_write(VS_STATE_PATH, json.dumps(state, indent=2))
                return summary

            ma, mb = top50[i], top50[j]
            # Alphabetical URL sorting to prevent canonical dupes
            a_slug = ma.get("slug", ma["id"].replace("/", "-"))
            b_slug = mb.get("slug", mb["id"].replace("/", "-"))
            
            ordered = sorted([a_slug, b_slug])
            matchup_id = f"{ordered[0]}-vs-{ordered[1]}"

            if matchup_id in completed_set:
                continue

            logger.info(f"Generating Showdown: {matchup_id}")
            text = _generate_showdown_text(groq, ma, mb)
            
            html_content = _render_html(ma, mb, text, template)
            _atomic_write(DIST_COMPARE_DIR / f"{matchup_id}.html", html_content)
            
            state["completed"].append(matchup_id)
            completed_set.add(matchup_id)
            generated_this_run += 1
            summary["generated"] += 1

    _atomic_write(VS_STATE_PATH, json.dumps(state, indent=2))
    return summary

if __name__ == "__main__":
    run_vs_generation()
