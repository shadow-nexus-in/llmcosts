"""
GODMODE V8 — Page Generator
Generates 300 Mega-Pages (HTML + Markdown) with:
- V6 Depth (6 AI-generated sections per model)
- 25 FAQ entries per model
- Top-5 competitor comparison table
- Schema.org Dataset + FAQPage JSON-LD
- Incremental builds (only regenerates changed pages)
- Atomic writes — never corrupts live site
"""
from __future__ import annotations

import html
import json
import logging
import os
import re
import shutil
import time
from pathlib import Path
from typing import Optional

from src.core.groq_client import GroqEngine

logger = logging.getLogger(__name__)

MODELS_JSON_PATH = Path("data/models.json")
DIST_MODELS_DIR = Path("dist/models")
DIST_COMPARE_DIR = Path("dist/compare")
TEMPLATE_PATH = Path("templates/model_page.html")
BUILD_STATE_PATH = Path("data/checkpoint.json")
SITE_URL = os.getenv("SITE_URL", "https://llmcosts.dev")
AFFILIATE_BASE = "https://openrouter.ai/?ref=llmcosts"

SYSTEM_PROMPT = (
    "You are a senior AI infrastructure engineer and technical writer. "
    "Write precise, data-driven content for an LLM pricing registry. "
    "Be factual, technical, and cite the exact numbers provided. "
    "Format all outputs in clean Markdown."
)


def _sanitize(value) -> str:
    """Sanitize any value for safe HTML injection."""
    return html.escape(str(value)) if value is not None else "N/A"


def _load_models() -> list[dict]:
    try:
        data = json.loads(MODELS_JSON_PATH.read_text(encoding="utf-8"))
        models = [m for m in data.get("models", []) if m.get("id")]
        for m in models:
            if m.get("pricing") is None: m["pricing"] = {}
            if m.get("benchmarks") is None: m["benchmarks"] = {}
        return models
    except Exception as e:
        logger.error(f"Cannot load models.json: {e}")
        return []


def _load_build_state() -> dict:
    try:
        if BUILD_STATE_PATH.exists():
            return json.loads(BUILD_STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        pass
    return {}


def _save_build_state(state: dict) -> None:
    try:
        tmp = BUILD_STATE_PATH.with_suffix(".tmp")
        tmp.write_text(json.dumps(state, indent=2), encoding="utf-8")
        tmp.replace(BUILD_STATE_PATH)
    except Exception as e:
        logger.warning(f"Could not save build state: {e}")


def _page_needs_rebuild(model: dict, state: dict) -> bool:
    mid = model.get("id") or ""
    slug = model.get("slug") or mid.replace("/", "-")
    html_path = DIST_MODELS_DIR / f"{slug}.html"
    # Always build if page doesn't exist yet
    if not html_path.exists():
        return True
    # Rebuild if pricing changed since last build
    last_price = state.get("prices", {}).get(mid)
    current_price = (model.get("pricing") or {}).get("input_per_1m")
    # If both are None (unpried model), treat as unchanged to avoid rebuilding every run
    if last_price is None and current_price is None:
        return False
    return last_price != current_price


def _format_price(value) -> str:
    if value is None:
        return "N/A"
    try:
        return f"${float(value):.4f}"
    except (ValueError, TypeError):
        return "N/A"


def _build_model_context(model: dict, all_models: list[dict]) -> str:
    """Build a rich, structured data context string to feed Groq."""
    p = model.get("pricing") or {}
    b = model.get("benchmarks") or {}
    comps = model.get("competing_models") or []

    # Build competitor pricing table
    comp_rows = []
    model_map = {m["id"]: m for m in all_models if m.get("id")}
    for cid in comps[:5]:
        cm = model_map.get(cid)
        if cm:
            cp = cm.get("pricing") or {}
            comp_rows.append(
                f"- {cm.get('name', cid)}: "
                f"${cp.get('input_per_1m', 'N/A')}/1M input, "
                f"${cp.get('output_per_1m', 'N/A')}/1M output"
            )
    comp_table = "\n".join(comp_rows) if comp_rows else "No direct competitors listed."

    ctx = f"""
MODEL: {model.get('name', 'Unknown')} ({model.get('id', '')})
Provider: {model.get('provider_name', 'Unknown')}
Release Date: {model.get('release_date', 'Unknown')}
Tier: {model.get('tier', 'Unknown')} | Open Source: {model.get('open_source', False)}

PRICING:
- Input: ${p.get('input_per_1m', 'N/A')} per 1M tokens
- Output: ${p.get('output_per_1m', 'N/A')} per 1M tokens
- Cached Input: ${p.get('cached_input_per_1m', 'N/A')} per 1M tokens
- Batch Input: ${p.get('batch_input_per_1m', 'N/A')} per 1M tokens

CONTEXT & LIMITS:
- Context Window: {f"{model.get('context_window'):,}" if model.get('context_window') else 'Pending'} tokens
- Max Output: {f"{model.get('max_output_tokens'):,}" if model.get('max_output_tokens') else 'Pending'} tokens
- Knowledge Cutoff: {model.get('knowledge_cutoff', 'N/A')}

BENCHMARKS:
- MMLU: {b.get('mmlu', 'N/A')}
- HumanEval: {b.get('humaneval', 'N/A')}
- LMSYS Arena ELO: {b.get('arena_elo', 'N/A')}
- GSM8K: {b.get('gsm8k', 'N/A')}

CAPABILITIES: {', '.join(str(c) for c in (model.get('capabilities') or []) if c)}
BEST FOR: {', '.join(str(u) for u in (model.get('use_cases') or []) if u)}
NOT GOOD FOR: {', '.join(str(n) for n in (model.get('not_good_for') or []) if n)}

COST EXAMPLES:
- 1,000 calls (avg 500 tokens): ${(model.get('cost_examples') or {}).get('1k_calls_avg_500_tokens', 'N/A')}
- 10,000 calls: ${(model.get('cost_examples') or {}).get('10k_calls_avg_500_tokens', 'N/A')}
- 100,000 calls: ${(model.get('cost_examples') or {}).get('100k_calls_avg_500_tokens', 'N/A')}

TOP COMPETITORS:
{comp_table}
"""
    return ctx.strip()


def _generate_page_content(groq: GroqEngine, model: dict, all_models: list[dict]) -> Optional[dict]:
    """Generate all 6 sections for a single model page using Groq."""
    ctx = _build_model_context(model, all_models)
    name = model.get("name", "Unknown")

    sections = {}

    # Section 1: Overview
    text = groq.generate(
        SYSTEM_PROMPT,
        f"Write a 3-paragraph technical overview of {name} for developers. Include its architecture, main strengths, and primary use-cases. Data:\n{ctx}",
        max_tokens=400,
    )
    sections["overview"] = text or f"{name} is an AI language model providing text generation capabilities."

    if groq.all_keys_exhausted():
        return None

    # Section 2: Pricing Deep-Dive
    text = groq.generate(
        SYSTEM_PROMPT,
        f"Write a detailed pricing analysis for {name}. Explain the cost structure, when to use cached tokens, batch API savings, and cost at scale (1k/10k/100k API calls). Data:\n{ctx}",
        max_tokens=400,
    )
    sections["pricing_analysis"] = text or "See pricing table above for detailed costs."

    if groq.all_keys_exhausted():
        return sections

    # Section 3: Benchmark Analysis
    text = groq.generate(
        SYSTEM_PROMPT,
        f"Analyze the benchmark performance of {name}. Explain what the MMLU, HumanEval, and Arena ELO scores mean for real-world use. Data:\n{ctx}",
        max_tokens=350,
    )
    sections["benchmark_analysis"] = text or "See benchmark table for scores."

    if groq.all_keys_exhausted():
        return sections

    # Section 4: Competitor Comparison
    text = groq.generate(
        SYSTEM_PROMPT,
        f"Write a detailed comparison of {name} against its top competitors. Include price differences, performance trade-offs, and when to choose each model. Data:\n{ctx}",
        max_tokens=500,
    )
    sections["comparison"] = text or "See comparison table below."

    if groq.all_keys_exhausted():
        return sections

    # Section 5: Best Use Cases
    text = groq.generate(
        SYSTEM_PROMPT,
        f"Write practical advice on the top 5 best use cases for {name}. Include specific code integration examples mentioning OpenRouter. Data:\n{ctx}",
        max_tokens=400,
    )
    sections["use_cases"] = text or "See use cases list below."

    if groq.all_keys_exhausted():
        return sections

    # Section 6: 25 FAQs
    text = groq.generate(
        SYSTEM_PROMPT,
        f"Generate exactly 25 FAQ pairs (Q: and A:) about {name} pricing, performance, and integration. Each answer should be 1-2 sentences with specific numbers. Data:\n{ctx}",
        max_tokens=800,
    )
    sections["faqs_raw"] = text or ""

    return sections


def _parse_faqs(raw: str) -> list[dict]:
    """Parse FAQ text into structured Q&A pairs."""
    faqs = []
    lines = raw.strip().split("\n")
    current_q = None
    for line in lines:
        line = line.strip()
        if line.lower().startswith("q:") or line.lower().startswith("q."):
            current_q = line[2:].strip().lstrip("0123456789. )")
        elif (line.lower().startswith("a:") or line.lower().startswith("a.")) and current_q:
            answer = line[2:].strip()
            if current_q and answer:
                faqs.append({"question": current_q, "answer": answer})
            current_q = None
    return faqs[:25]


def _render_html(model: dict, sections: dict, template: str, model_map: dict) -> str:
    """Renders the model HTML page using the template."""
    p = model.get("pricing") or {}
    b = model.get("benchmarks") or {}
    name = _sanitize(model.get("name", "Unknown"))
    provider = _sanitize(model.get("provider_name", "Unknown"))
    slug = model.get("slug") or model["id"].replace("/", "-")

    faqs = _parse_faqs(sections.get("faqs_raw", ""))

    # Build FAQ HTML
    faq_items_html = ""
    for faq in faqs:
        faq_items_html += f"""
        <div class="faq-item">
            <h3 class="faq-question">{_sanitize(faq['question'])}</h3>
            <p class="faq-answer">{_sanitize(faq['answer'])}</p>
        </div>"""

    # Build Schema.org JSON-LD
    faq_schema_items = [
        {"@type": "Question",
         "name": faq["question"],
         "acceptedAnswer": {"@type": "Answer", "text": faq["answer"]}}
        for faq in faqs
    ]
    schema_dataset = {
        "@context": "https://schema.org",
        "@type": ["Dataset", "SoftwareApplication"],
        "name": f"{model.get('name', 'Unknown')} API Pricing",
        "description": f"Complete pricing, benchmarks and API cost analysis for {model.get('name', 'Unknown')} by {model.get('provider_name', 'Unknown')}.",
        "url": f"{SITE_URL}/models/{slug}",
        "keywords": [model.get("name"), model.get("provider_name")] + model.get("tags", []),
        "dateModified": time.strftime("%Y-%m-%d"),
        "publisher": {"@type": "Organization", "name": "LLMCosts.dev"},
    }
    schema_faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_schema_items,
    }

    # Competitor table rows — use pre-loaded model_map, NOT disk re-read
    comp_rows_html = ""
    for cid in model.get("competing_models") or []:
        if len(comp_rows_html) > 4: break  # limit to 5
        cm = model_map.get(cid) or {}
        if cm:
            cp = cm.get("pricing") or {}
            cslug = cm.get("slug") or cid.replace("/", "-")
            comp_rows_html += f"""
            <tr>
                <td><a href="/models/{_sanitize(cslug)}">{_sanitize(cm.get('name', cid))}</a></td>
                <td>{_format_price(cp.get('input_per_1m'))}</td>
                <td>{_format_price(cp.get('output_per_1m'))}</td>
                <td>{(cm.get('benchmarks') or {}).get('arena_elo', 'N/A')}</td>
                <td>{_sanitize(cm.get('tier', 'N/A'))}</td>
            </tr>"""

    replacements = {
        "{{MODEL_NAME}}": name,
        "{{MODEL_SLUG}}": _sanitize(slug),
        "{{PROVIDER_NAME}}": provider,
        "{{MODEL_ID}}": _sanitize(model.get("id", "")),
        "{{TIER}}": _sanitize(model.get("tier", "N/A")),
        "{{OPEN_SOURCE}}": "Yes [PASS]" if model.get("open_source") else "No [FAIL]",
        "{{SELF_HOSTABLE}}": "Yes [PASS]" if model.get("self_hostable") else "No [FAIL]",
        "{{RELEASE_DATE}}": _sanitize(model.get("release_date", "N/A")),
        "{{KNOWLEDGE_CUTOFF}}": _sanitize(model.get("knowledge_cutoff", "N/A")),
        "{{CONTEXT_WINDOW}}": f"{model.get('context_window') or 0:,}" if model.get('context_window') else "Pending",
        "{{MAX_OUTPUT}}": f"{model.get('max_output_tokens') or 0:,}" if model.get('max_output_tokens') else "Pending",
        "{{INPUT_PRICE}}": _format_price(p.get("input_per_1m")),
        "{{OUTPUT_PRICE}}": _format_price(p.get("output_per_1m")),
        "{{CACHED_PRICE}}": _format_price(p.get("cached_input_per_1m")),
        "{{BATCH_INPUT}}": _format_price(p.get("batch_input_per_1m")),
        "{{BATCH_OUTPUT}}": _format_price(p.get("batch_output_per_1m")),
        "{{ARENA_ELO}}": str(b.get("arena_elo", "N/A")),
        "{{MMLU}}": str(b.get("mmlu", "N/A")),
        "{{HUMANEVAL}}": str(b.get("humaneval", "N/A")),
        "{{OVERVIEW}}": sections.get("overview", ""),
        "{{PRICING_ANALYSIS}}": sections.get("pricing_analysis", ""),
        "{{BENCHMARK_ANALYSIS}}": sections.get("benchmark_analysis", ""),
        "{{COMPARISON}}": sections.get("comparison", ""),
        "{{USE_CASES}}": sections.get("use_cases", ""),
        "{{FAQ_ITEMS}}": faq_items_html,
        "{{SCHEMA_DATASET}}": json.dumps(schema_dataset, ensure_ascii=False),
        "{{SCHEMA_FAQ}}": json.dumps(schema_faq, ensure_ascii=False),
        "{{COMPETITOR_ROWS}}": comp_rows_html,
        "{{CAPABILITIES}}": " ".join(
            f'<span class="cap-tag">{html.escape(str(c))}</span>'
            for c in (model.get("capabilities") or []) if c
        ),
        "{{AFFILIATE_LINK}}": AFFILIATE_BASE,
        "{{SITE_URL}}": SITE_URL,
        "{{LAST_VERIFIED}}": _sanitize(model.get("last_verified", "N/A")),
        "{{COST_1K}}": str((model.get("cost_examples") or {}).get("1k_calls_avg_500_tokens", "N/A")),
        "{{COST_10K}}": str((model.get("cost_examples") or {}).get("10k_calls_avg_500_tokens", "N/A")),
        "{{COST_100K}}": str((model.get("cost_examples") or {}).get("100k_calls_avg_500_tokens", "N/A")),
        "{{PRICE_TREND}}": _sanitize(model.get("price_trend", "N/A")),
        "{{DATA_CONFIDENCE}}": _sanitize(model.get("data_confidence", "N/A")),
    }

    rendered = template
    for placeholder, value in replacements.items():
        rendered = rendered.replace(placeholder, str(value))
    return rendered


def _render_markdown(model: dict, sections: dict) -> str:
    """Renders the .md phantom route for AI crawlers."""
    p = model.get("pricing", {})
    b = model.get("benchmarks", {})
    name = model.get("name", "Unknown")
    provider = model.get("provider_name", "Unknown")
    faqs = _parse_faqs(sections.get("faqs_raw", ""))

    faq_md = "\n".join(
        f"**Q: {faq['question']}**\nA: {faq['answer']}\n"
        for faq in faqs
    )

    return f"""# {name} API Pricing & Analysis | LLMCosts.dev

> Source: [LLMCosts.dev](https://llmcosts.dev) — Updated {time.strftime('%Y-%m-%d')}
> Route cheapest: [OpenRouter]({AFFILIATE_BASE})

## Overview
{sections.get('overview', '')}

## Pricing (USD per 1M tokens)
| Metric | Price |
|--------|-------|
| Input | ${p.get('input_per_1m', 'N/A')} |
| Output | ${p.get('output_per_1m', 'N/A')} |
| Cached Input | ${p.get('cached_input_per_1m', 'N/A')} |
| Batch Input | ${p.get('batch_input_per_1m', 'N/A')} |
| Batch Output | ${p.get('batch_output_per_1m', 'N/A')} |

## Pricing Analysis
{sections.get('pricing_analysis', '')}

## Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMLU | {b.get('mmlu', 'N/A')} |
| HumanEval | {b.get('humaneval', 'N/A')} |
| LMSYS Arena ELO | {b.get('arena_elo', 'N/A')} |
| ARC | {b.get('arc', 'N/A')} |

## Benchmark Analysis
{sections.get('benchmark_analysis', '')}

## Competitor Comparison
{sections.get('comparison', '')}

## Best Use Cases
{sections.get('use_cases', '')}

## Frequently Asked Questions
{faq_md}

---
*Data verified: {model.get('last_verified', 'N/A')} | Confidence: {model.get('data_confidence', 'N/A')}*
*[Get API Access via OpenRouter]({AFFILIATE_BASE})*
"""


def _atomic_write(path: Path, content: str) -> None:
    """Write file atomically using temp file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    try:
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(path)
    except Exception as e:
        tmp.unlink(missing_ok=True)
        raise e


def run_page_generation(single_model: Optional[str] = None) -> dict:
    """
    Main entry point. Generates all model Mega-Pages.
    Pass single_model='gpt-4o' for dry-run testing on one model.
    """
    summary = {"generated": 0, "skipped": 0, "failed": 0, "keys_exhausted": False}

    logger.info("=" * 60)
    logger.info("PAGE GENERATOR: Starting Mega-Page generation...")

    DIST_MODELS_DIR.mkdir(parents=True, exist_ok=True)
    DIST_COMPARE_DIR.mkdir(parents=True, exist_ok=True)

    try:
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        logger.error(f"Template not found at {TEMPLATE_PATH}. Cannot generate pages.")
        summary["failed"] += 1
        return summary

    models = _load_models()
    if not models:
        logger.error("No models loaded.")
        return summary

    if single_model:
        models = [m for m in models if m.get("slug") == single_model or m.get("id") == single_model]
        if not models:
            logger.error(f"Model '{single_model}' not found.")
            return summary

    build_state = _load_build_state()

    # Build model_map ONCE here — not per model inside _render_html
    model_map = {m["id"]: m for m in models}

    try:
        groq = GroqEngine()
    except EnvironmentError as e:
        logger.error(f"Groq initialisation failed: {e}")
        summary["failed"] += 1
        return summary

    for i, model in enumerate(models, 1):
        mid = model.get("id", "unknown")
        slug = model.get("slug", mid.replace("/", "-"))

        if groq.all_keys_exhausted():
            logger.warning("All Groq keys exhausted. Stopping page generation.")
            summary["keys_exhausted"] = True
            break

        if not _page_needs_rebuild(model, build_state):
            logger.debug(f"[{i}/{len(models)}] SKIP: {mid} (unchanged)")
            summary["skipped"] += 1
            continue

        logger.info(f"[{i}/{len(models)}] GENERATING: {mid}")

        try:
            sections = _generate_page_content(groq, model, models)
            if sections is None:
                logger.warning(f"Generation returned None for {mid}. Skipping.")
                summary["failed"] += 1
                continue

            # Write HTML
            html_content = _render_html(model, sections, template, model_map)
            _atomic_write(DIST_MODELS_DIR / f"{slug}.html", html_content)

            # Write Markdown phantom route
            md_content = _render_markdown(model, sections)
            _atomic_write(DIST_MODELS_DIR / f"{slug}.md", md_content)

            # Save price to build state for incremental detection
            build_state.setdefault("prices", {})[mid] = (model.get("pricing") or {}).get("input_per_1m")
            _save_build_state(build_state)

            summary["generated"] += 1
            logger.info(f"  [PASS] Done: dist/models/{slug}.html + .md")

        except Exception as e:
            logger.error(f"Failed to generate page for {mid}: {e}", exc_info=True)
            summary["failed"] += 1
            continue

    logger.info(f"Page generation complete: {summary}")
    return summary
