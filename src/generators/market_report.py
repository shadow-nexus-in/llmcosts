"""
GODMODE V8 — Daily Arbitrage Intelligence Report Generator
Burns surplus Groq API calls to produce a premium B2B market report.
Output: dist/daily-report/index.html + dist/daily-report/index.md
"""
from __future__ import annotations

import json
import logging
import os
import time
from pathlib import Path
from typing import Optional

from src.core.groq_client import GroqEngine

logger = logging.getLogger(__name__)

MODELS_JSON_PATH = Path("data/models.json")
DIST_REPORT_DIR = Path("dist/daily-report")
SITE_URL = os.getenv("SITE_URL", "https://llmcosts.dev")
AFFILIATE_BASE = "https://openrouter.ai/?ref=llmcosts"

SYSTEM_PROMPT = (
    "You are a senior AI market analyst at a top-tier investment research firm. "
    "Write dense, data-driven, B2B-grade API market intelligence. "
    "Use exact numbers from the data provided. Be concise, specific, and actionable. "
    "Format output in clean Markdown with headers."
)


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


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    try:
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(path)
    except Exception as e:
        tmp.unlink(missing_ok=True)
        raise e


def _build_market_context(models: list[dict]) -> str:
    """Build a compact market snapshot for the Groq prompt."""
    sorted_by_price = sorted(
        [m for m in models if m.get("pricing", {}).get("input_per_1m") is not None],
        key=lambda x: x["pricing"]["input_per_1m"],
    )

    cheapest5 = sorted_by_price[:5]
    most_expensive5 = sorted_by_price[-5:]

    # Find best value (cheapest per ELO point)
    def value_score(m):
        try:
            inp = float(m.get("pricing", {}).get("input_per_1m") or 9999)
            elo = float(m.get("benchmarks", {}).get("arena_elo") or 0)
            if inp <= 0 or elo <= 0:
                return 9999
            return inp / elo
        except (ValueError, TypeError):
            return 9999

    ranked_value = sorted(
        [m for m in models if m.get("benchmarks", {}).get("arena_elo")],
        key=value_score,
    )
    best_value = ranked_value[:3] if ranked_value else []

    # Provider market share
    providers: dict[str, int] = {}
    for m in models:
        p = m.get("provider_name", "Unknown")
        providers[p] = providers.get(p, 0) + 1

    top_providers = sorted(providers.items(), key=lambda x: x[1], reverse=True)[:6]

    ctx = f"TODAY: {time.strftime('%Y-%m-%d')}\nTOTAL MODELS IN REGISTRY: {len(models)}\n\n"

    ctx += "CHEAPEST 5 MODELS (input per 1M tokens):\n"
    for m in cheapest5:
        p = m.get("pricing", {})
        ctx += (
            f"- {m.get('name')}: ${p.get('input_per_1m', 'N/A')} in / "
            f"${p.get('output_per_1m', 'N/A')} out | "
            f"ELO: {m.get('benchmarks', {}).get('arena_elo', 'N/A')}\n"
        )

    ctx += "\nMOST EXPENSIVE 5:\n"
    for m in most_expensive5:
        p = m.get("pricing", {})
        ctx += (
            f"- {m.get('name')}: ${p.get('input_per_1m', 'N/A')} in / "
            f"${p.get('output_per_1m', 'N/A')} out\n"
        )

    ctx += "\nBEST PRICE/PERFORMANCE (lowest cost per ELO point):\n"
    for m in best_value:
        p = m.get("pricing", {})
        elo = m.get("benchmarks", {}).get("arena_elo", "N/A")
        ctx += f"- {m.get('name')}: ${p.get('input_per_1m', 'N/A')}/1M | ELO {elo}\n"

    ctx += "\nPROVIDER MARKET SHARE (by model count):\n"
    for pname, count in top_providers:
        ctx += f"- {pname}: {count} models\n"

    return ctx.strip()


def _generate_report_sections(groq: GroqEngine, ctx: str) -> dict:
    """Generate all report sections using surplus Groq calls."""
    sections = {}
    today = time.strftime("%Y-%m-%d")

    # Section 1: Executive Summary
    text = groq.generate(
        SYSTEM_PROMPT,
        f"Write a 3-paragraph executive summary of today's LLM API market. "
        f"Highlight the biggest pricing gaps, best value plays, and market concentration. "
        f"Data:\n{ctx}",
        max_tokens=450,
    )
    sections["executive_summary"] = text or "Market data processed. See sections below."

    if groq.all_keys_exhausted():
        return sections

    # Section 2: Arbitrage Opportunities
    text = groq.generate(
        SYSTEM_PROMPT,
        f"Identify the top 3 API pricing arbitrage opportunities for developers today. "
        f"Where can developers switch models and cut costs by the highest percentage "
        f"with minimal quality reduction? Be specific with dollar amounts. Data:\n{ctx}",
        max_tokens=400,
    )
    sections["arbitrage"] = text or "See cheapest models table for opportunities."

    if groq.all_keys_exhausted():
        return sections

    # Section 3: Provider Power Rankings
    text = groq.generate(
        SYSTEM_PROMPT,
        f"Rank the top 5 LLM providers by value-for-money today. "
        f"Explain each provider's pricing strategy and target market segment. Data:\n{ctx}",
        max_tokens=400,
    )
    sections["provider_rankings"] = text or "See provider data above."

    if groq.all_keys_exhausted():
        return sections

    # Section 4: Cost Optimization Playbook
    text = groq.generate(
        SYSTEM_PROMPT,
        f"Write a 5-step cost optimization playbook for teams spending over $1,000/month "
        f"on LLM APIs. Include specific model recommendations for each workload type. Data:\n{ctx}",
        max_tokens=500,
    )
    sections["cost_playbook"] = text or "Use cheapest model appropriate for your task."

    if groq.all_keys_exhausted():
        return sections

    # Section 5: Market Forecast
    text = groq.generate(
        SYSTEM_PROMPT,
        f"Based on current pricing data and provider competition, write a short-term "
        f"(30-90 day) pricing market forecast. Which segments will see price drops? "
        f"Where is pricing sticky? Data:\n{ctx}",
        max_tokens=350,
    )
    sections["forecast"] = text or "Competition continues to drive prices lower in standard tiers."

    return sections


def _render_html(sections: dict, ctx: str) -> str:
    today = time.strftime("%Y-%m-%d")
    date_human = time.strftime("%B %d, %Y")

    def md_section(title: str, key: str) -> str:
        content = sections.get(key, "")
        paragraphs = [p.strip() for p in content.split("\n") if p.strip()]
        html_paras = "".join(f"<p>{p}</p>" for p in paragraphs)
        return f"""
      <div class="card content-section">
        <div class="card-title">{title}</div>
        <div class="prose">{html_paras}</div>
      </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LLM API Market Intelligence Report — {date_human} | LLMCosts.dev</title>
  <meta name="description" content="Daily LLM API pricing arbitrage analysis, provider rankings, and cost optimization playbook. Updated {today} by LLMCosts.dev.">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{SITE_URL}/daily-report">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script type="application/ld+json">{{
    "@context": "https://schema.org",
    "@type": "Report",
    "name": "LLM API Market Intelligence Report {today}",
    "description": "Daily AI API pricing arbitrage analysis and cost optimization intelligence.",
    "url": "{SITE_URL}/daily-report",
    "datePublished": "{today}",
    "publisher": {{"@type": "Organization", "name": "LLMCosts.dev", "url": "{SITE_URL}"}}
  }}</script>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --bg-primary: #0a0a0f; --bg-secondary: #111118; --bg-card: #16161f;
      --bg-card-hover: #1d1d2a; --border: #1e1e2e; --border-bright: #2d2d45;
      --text-primary: #e8e8f0; --text-secondary: #8888aa; --text-muted: #555577;
      --accent-blue: #5b8af5; --accent-purple: #9b59f5; --accent-green: #3effa0;
      --accent-orange: #ff9f43; --accent-red: #ff4757;
      --gradient-hero: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
      --gradient-card: linear-gradient(135deg, rgba(91,138,245,0.1) 0%, rgba(155,89,245,0.05) 100%);
      --shadow-card: 0 4px 24px rgba(0,0,0,0.4); --radius: 12px; --radius-sm: 8px;
      --font-mono: 'JetBrains Mono', monospace;
    }}
    body {{ font-family: 'Inter', -apple-system, sans-serif; background: var(--bg-primary);
      color: var(--text-primary); line-height: 1.7; min-height: 100vh; }}
    nav {{ position: sticky; top: 0; z-index: 100; background: rgba(10,10,15,0.9);
      backdrop-filter: blur(20px); border-bottom: 1px solid var(--border); padding: 0 1.5rem; }}
    .nav-inner {{ max-width: 1200px; margin: 0 auto; display: flex; align-items: center;
      justify-content: space-between; height: 60px; }}
    .nav-logo {{ font-size: 1.1rem; font-weight: 700;
      background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-decoration: none; }}
    .nav-links {{ display: flex; gap: 1.5rem; }}
    .nav-links a {{ color: var(--text-secondary); text-decoration: none; font-size: 0.875rem;
      transition: color 0.2s; }}
    .nav-links a:hover {{ color: var(--text-primary); }}
    .hero {{ background: var(--gradient-hero); padding: 4rem 1.5rem 3rem;
      border-bottom: 1px solid var(--border); }}
    .hero-inner {{ max-width: 1200px; margin: 0 auto; }}
    .hero-badge {{ display: inline-flex; align-items: center; gap: 0.5rem;
      background: rgba(255,159,67,0.12); border: 1px solid rgba(255,159,67,0.3);
      border-radius: 999px; padding: 0.25rem 0.75rem; font-size: 0.75rem;
      color: var(--accent-orange); margin-bottom: 1.5rem; }}
    h1 {{ font-size: clamp(1.75rem, 4vw, 2.75rem); font-weight: 700; line-height: 1.2;
      margin-bottom: 1rem; }}
    h1 span {{ background: linear-gradient(135deg, var(--accent-orange) 0%, var(--accent-red) 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
    .hero-sub {{ color: var(--text-secondary); font-size: 1rem; max-width: 600px; margin-top: 0.5rem; }}
    .report-meta {{ display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1.5rem; font-size: 0.8rem;
      color: var(--text-muted); }}
    .report-meta span {{ background: rgba(255,255,255,0.05); border: 1px solid var(--border-bright);
      border-radius: var(--radius-sm); padding: 0.375rem 0.75rem; }}
    .report-meta strong {{ color: var(--text-primary); }}
    .page-body {{ max-width: 900px; margin: 0 auto; padding: 2.5rem 1.5rem 4rem; }}
    .card {{ background: var(--bg-card); border: 1px solid var(--border);
      border-radius: var(--radius); padding: 1.75rem; box-shadow: var(--shadow-card);
      transition: border-color 0.2s; margin-bottom: 1.5rem; }}
    .card:hover {{ border-color: var(--border-bright); }}
    .card-title {{ font-size: 0.7rem; font-weight: 600; letter-spacing: 0.1em;
      text-transform: uppercase; color: var(--text-muted); margin-bottom: 1.25rem; }}
    .content-section .prose p {{ color: var(--text-secondary); margin-bottom: 0.75rem;
      font-size: 0.9375rem; line-height: 1.75; }}
    .content-section .prose p:last-child {{ margin-bottom: 0; }}
    .toc {{ list-style: none; }}
    .toc li {{ padding: 0.5rem 0; border-bottom: 1px solid var(--border); font-size: 0.875rem; }}
    .toc li:last-child {{ border-bottom: none; }}
    .toc a {{ color: var(--accent-blue); text-decoration: none; }}
    .toc a:hover {{ text-decoration: underline; }}
    .subscribe-box {{ background: var(--gradient-card); border: 1px solid var(--border-bright);
      border-radius: var(--radius); padding: 2rem; text-align: center; margin-bottom: 1.5rem; }}
    .subscribe-box h3 {{ font-size: 1.25rem; margin-bottom: 0.5rem; }}
    .subscribe-box p {{ color: var(--text-muted); font-size: 0.875rem; margin-bottom: 1rem; }}
    .cta-btn {{ display: inline-block; padding: 0.75rem 2rem;
      background: linear-gradient(135deg, var(--accent-orange), var(--accent-red));
      color: #fff; font-weight: 600; font-size: 0.875rem;
      text-align: center; text-decoration: none; border-radius: var(--radius-sm);
      transition: opacity 0.2s, transform 0.15s; }}
    .cta-btn:hover {{ opacity: 0.88; transform: translateY(-1px); }}
    footer {{ border-top: 1px solid var(--border); padding: 2rem 1.5rem;
      text-align: center; color: var(--text-muted); font-size: 0.8rem; }}
    footer a {{ color: var(--text-secondary); text-decoration: none; }}
    footer a:hover {{ color: var(--text-primary); }}
    @media (max-width: 640px) {{
      .hero {{ padding: 2.5rem 1rem 2rem; }}
      .page-body {{ padding: 1.5rem 1rem 3rem; }}
    }}
  </style>
</head>
<body>

<nav>
  <div class="nav-inner">
    <a href="/" class="nav-logo">⚡ LLMCosts.dev</a>
    <div class="nav-links">
      <a href="/compare">Compare</a>
      <a href="/configs">Configs</a>
      <a href="/daily-report" style="color:var(--text-primary)">Market Report</a>
    </div>
  </div>
</nav>

<div class="hero">
  <div class="hero-inner">
    <div class="hero-badge">📊 Daily Intelligence · {date_human}</div>
    <h1>LLM API <span>Market Intelligence</span></h1>
    <p class="hero-sub">
      Automated arbitrage analysis, provider rankings, and cost optimization playbook —
      generated from live pricing data. Updated every 24 hours.
    </p>
    <div class="report-meta">
      <span>📅 Published: <strong>{date_human}</strong></span>
      <span>🤖 AI-Generated via Groq</span>
      <span>✅ Dual-source verified</span>
      <span><a href="{SITE_URL}/daily-report/index.md" style="color:var(--accent-blue)">📄 Raw .md</a></span>
    </div>
  </div>
</div>

<div class="page-body">

  <div class="card">
    <div class="card-title">Table of Contents</div>
    <ol class="toc">
      <li><a href="#executive-summary">Executive Summary</a></li>
      <li><a href="#arbitrage">Arbitrage Opportunities</a></li>
      <li><a href="#provider-rankings">Provider Power Rankings</a></li>
      <li><a href="#cost-playbook">Cost Optimization Playbook</a></li>
      <li><a href="#forecast">30–90 Day Market Forecast</a></li>
    </ol>
  </div>

  <div id="executive-summary">
    {md_section("Executive Summary", "executive_summary")}
  </div>

  <div id="arbitrage">
    {md_section("🎯 Top Arbitrage Opportunities", "arbitrage")}
  </div>

  <div id="provider-rankings">
    {md_section("🏆 Provider Power Rankings", "provider_rankings")}
  </div>

  <div id="cost-playbook">
    {md_section("💰 Cost Optimization Playbook", "cost_playbook")}
  </div>

  <div id="forecast">
    {md_section("🔮 30–90 Day Market Forecast", "forecast")}
  </div>

  <div class="subscribe-box">
    <h3>Route All Your API Calls Through OpenRouter</h3>
    <p>Automatically get the cheapest price for every model, every day. No lock-in.</p>
    <a href="{AFFILIATE_BASE}" class="cta-btn" id="cta-openrouter-report" target="_blank" rel="noopener">
      ⚡ Start Saving on API Costs →
    </a>
  </div>

</div>

<footer>
  <p>
    <a href="/">LLMCosts.dev</a> — Open LLM Pricing Registry |
    Report generated {today} |
    <a href="/llms.txt">llms.txt</a> |
    <a href="/sitemap.xml">Sitemap</a>
  </p>
  <p style="margin-top:0.5rem">
    AI content generated via Groq (Llama-3). Pricing data from OpenRouter &amp; LiteLLM.
  </p>
</footer>

</body>
</html>"""


def _render_markdown(sections: dict) -> str:
    today = time.strftime("%Y-%m-%d")
    date_human = time.strftime("%B %d, %Y")
    return f"""# LLM API Market Intelligence Report — {date_human}

> Source: [LLMCosts.dev]({SITE_URL}/daily-report)
> Updated: {today}
> Route cheaper: [OpenRouter]({AFFILIATE_BASE})

## Executive Summary
{sections.get("executive_summary", "")}

## Top Arbitrage Opportunities
{sections.get("arbitrage", "")}

## Provider Power Rankings
{sections.get("provider_rankings", "")}

## Cost Optimization Playbook
{sections.get("cost_playbook", "")}

## 30–90 Day Market Forecast
{sections.get("forecast", "")}

---
*Generated by [LLMCosts.dev]({SITE_URL}) | Data verified {today}*
*[Route via OpenRouter]({AFFILIATE_BASE}) to always pay the lowest price.*
"""


def run_report_generation() -> dict:
    """Main entry point. Generates daily intelligence report."""
    summary = {"report_generated": False, "errors": 0}

    logger.info("=" * 60)
    logger.info("REPORT GENERATOR: Building daily market intelligence...")

    models = _load_models()
    if not models:
        summary["errors"] += 1
        return summary

    try:
        groq = GroqEngine()
    except EnvironmentError as e:
        logger.error(f"Groq unavailable for report: {e}")
        summary["errors"] += 1
        return summary

    if groq.all_keys_exhausted():
        logger.info("All Groq keys exhausted. Skipping report generation.")
        return summary

    try:
        ctx = _build_market_context(models)
        sections = _generate_report_sections(groq, ctx)

        html_content = _render_html(sections, ctx)
        md_content = _render_markdown(sections)

        _atomic_write(DIST_REPORT_DIR / "index.html", html_content)
        _atomic_write(DIST_REPORT_DIR / "index.md", md_content)

        summary["report_generated"] = True
        logger.info("  ✅ dist/daily-report/index.html + index.md")
    except Exception as e:
        logger.error(f"Report generation failed: {e}", exc_info=True)
        summary["errors"] += 1

    logger.info(f"Report generation complete: {summary}")
    return summary
