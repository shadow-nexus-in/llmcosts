"""
GODMODE V8 — Homepage & Compare Page Generator
Generates the static landing page and model comparison table.
Zero external API required — pure data from models.json.
"""
from __future__ import annotations

import json
import logging
import os
import time
from pathlib import Path

logger = logging.getLogger(__name__)

MODELS_JSON_PATH = Path("data/models.json")
DIST_DIR = Path("dist")
SITE_URL = os.getenv("SITE_URL", "https://llmcosts.dev")
AFFILIATE_BASE = "https://openrouter.ai/?ref=llmcosts"


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


def _safe_price(val) -> str:
    if val is None:
        return "N/A"
    try:
        return f"${float(val):.4f}"
    except (ValueError, TypeError):
        return "N/A"


def _build_models_json_embed(models: list[dict]) -> str:
    """Serialise a compact version of models for the JS search engine."""
    compact = []
    for m in models:
        p = m.get("pricing") or {}
        b = m.get("benchmarks") or {}
        compact.append({
            "id": m.get("id", ""),
            "name": m.get("name", ""),
            "slug": m.get("slug", ""),
            "provider": m.get("provider_name", ""),
            "tier": m.get("tier", ""),
            "open_source": m.get("open_source", False),
            "context": m.get("context_window") or 0,
            "inp": p.get("input_per_1m"),
            "out": p.get("output_per_1m"),
            "cached": p.get("cached_input_per_1m"),
            "elo": b.get("arena_elo"),
            "mmlu": b.get("mmlu"),
            "capabilities": m.get("capabilities") or [],
        })
    return json.dumps(compact, ensure_ascii=False, separators=(",", ":"))


def _build_homepage(models: list[dict]) -> str:
    today = time.strftime("%Y-%m-%d")
    total = len(models)

    # Stats
    priced = [m for m in models if (m.get("pricing") or {}).get("input_per_1m") is not None]
    try:
        cheapest = min(priced, key=lambda m: float(m["pricing"]["input_per_1m"])) if priced else None
    except (ValueError, TypeError):
        cheapest = priced[0] if priced else None
    providers = len({m.get("provider_name") for m in models if m.get("provider_name")})
    oss_count = sum(1 for m in models if m.get("open_source"))

    cheapest_name = cheapest.get("name", "N/A") if cheapest else "N/A"
    cheapest_price = _safe_price((cheapest.get("pricing") or {}).get("input_per_1m")) if cheapest else "N/A"
    cheapest_slug = cheapest.get("slug", "") if cheapest else ""

    models_json = _build_models_json_embed(models)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LLM API Pricing Comparison 2026 — Compare 300 AI Models | LLMCosts.dev</title>
  <meta name="description" content="Compare real-time pricing for 300+ LLM APIs including GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro. Input/output token costs, benchmarks, and cost calculator. Updated daily.">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{SITE_URL}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

  <!-- Open Graph -->
  <meta property="og:title" content="LLM API Pricing Comparison 2026 | LLMCosts.dev">
  <meta property="og:description" content="Compare pricing for {total}+ AI models. Input costs, output costs, benchmarks. Updated {today}.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE_URL}">

  <script type="application/ld+json">{{
    "@context": "https://schema.org",
    "@type": "Dataset",
    "name": "LLM API Pricing Registry 2026",
    "description": "Complete pricing database for {total}+ large language model APIs. Input/output token costs, context windows, benchmarks, updated daily.",
    "url": "{SITE_URL}",
    "keywords": ["LLM pricing", "GPT-4 cost", "Claude API price", "AI token cost", "language model comparison"],
    "dateModified": "{today}",
    "publisher": {{"@type": "Organization", "name": "LLMCosts.dev", "url": "{SITE_URL}"}}
  }}</scrip    <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --bg-primary: #050508; --bg-secondary: #0d0d14; --bg-card: rgba(20, 20, 30, 0.4);
      --bg-card-hover: rgba(35, 35, 50, 0.6); --border: rgba(255, 255, 255, 0.08); 
      --border-bright: rgba(255, 255, 255, 0.15);
      --text-primary: #f8f8fc; --text-secondary: #9a9ab5; --text-muted: #656588;
      --accent-blue: #6d9efa; --accent-purple: #b37afc; --accent-green: #4effb0;
      --accent-orange: #ffb15c; --accent-red: #ff5e70;
      --font-mono: 'JetBrains Mono', monospace;
      --radius: 16px; --radius-sm: 10px;
      --shadow-card: 0 8px 32px rgba(0, 0, 0, 0.6);
      --shadow-neon: 0 0 20px rgba(109, 158, 250, 0.2);
    }}
    body {{ font-family: 'Inter', -apple-system, sans-serif; background: var(--bg-primary);
      color: var(--text-primary); line-height: 1.6; min-height: 100vh; }}

    /* ── Nav (Glassmorphism) ── */
    nav {{ position: sticky; top: 0; z-index: 100; background: rgba(5,5,8,0.7);
      backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border-bottom: 1px solid var(--border); padding: 0 1.5rem; }}
    .nav-inner {{ max-width: 1400px; margin: 0 auto; display: flex; align-items: center;
      justify-content: space-between; height: 60px; }}
    .nav-logo {{ font-size: 1.25rem; font-weight: 800; letter-spacing: -0.02em;
      background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple), var(--accent-green));
      background-size: 200% auto; animation: gradientShift 4s linear infinite;
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-decoration: none; }}
    @keyframes gradientShift {{ 0% {{background-position: 0% 50%;}} 50% {{background-position: 100% 50%;}} 100% {{background-position: 0% 50%;}} }}
    .nav-links {{ display: flex; gap: 1.5rem; align-items: center; }}
    .nav-links a {{ color: var(--text-secondary); text-decoration: none; font-size: 0.875rem;
      transition: color 0.3s; font-weight: 500; }}
    .nav-links a:hover {{ color: var(--text-primary); text-shadow: 0 0 10px rgba(255,255,255,0.3); }}
    .nav-badge {{ background: rgba(78,255,176,0.15); border: 1px solid rgba(78,255,176,0.3); color: var(--accent-green); font-size: 0.65rem;
      font-weight: 700; padding: 0.2rem 0.5rem; border-radius: 4px; margin-left: 0.4rem; box-shadow: 0 0 10px rgba(78,255,176,0.1); }}

    /* ── Hero (God-Tier Overhaul) ── */
    .hero {{ background: radial-gradient(circle at 50% -20%, rgba(109,158,250,0.15), transparent 60%), radial-gradient(circle at 100% 10%, rgba(179,122,252,0.1), transparent 50%), transparent;
      padding: 6rem 1.5rem 5rem; text-align: center; border-bottom: 1px solid var(--border);
      position: relative; overflow: hidden; }}
    .hero::before {{ content: ''; position: absolute; inset: 0;
      background: url('data:image/svg+xml;utf8,<svg width="40" height="40" xmlns="http://www.w3.org/2000/svg"><circle cx="2" cy="2" r="1" fill="rgba(255,255,255,0.03)"/></svg>');
      pointer-events: none; z-index: 0; }}
    .hero-badge {{ display: inline-flex; align-items: center; gap: 0.5rem;
      background: rgba(78,255,176,0.1); border: 1px solid rgba(78,255,176,0.3);
      border-radius: 999px; padding: 0.4rem 1.1rem; font-size: 0.75rem; font-weight: 600;
      color: var(--accent-green); margin-bottom: 2rem; position: relative; z-index: 1; box-shadow: 0 0 20px rgba(78,255,176,0.1); }}
    .pulse {{ width: 8px; height: 8px; border-radius: 50%; background: var(--accent-green);
      animation: pulseObj 2s infinite; box-shadow: 0 0 8px var(--accent-green); }}
    @keyframes pulseObj {{ 0%{{transform:scale(0.95);box-shadow:0 0 0 0 rgba(78,255,176,0.7);}} 70%{{transform:scale(1);box-shadow:0 0 0 6px rgba(78,255,176,0);}} 100%{{transform:scale(0.95);box-shadow:0 0 0 0 rgba(78,255,176,0);}} }}
    h1 {{ font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 800; line-height: 1.1;
      letter-spacing: -0.03em; margin-bottom: 1.5rem; position: relative; z-index: 1; }}
    h1 .gradient {{ background: linear-gradient(135deg, #ffffff 0%, var(--accent-blue) 40%, var(--accent-purple) 80%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0 4px 30px rgba(109,158,250,0.2); }}
    .hero-sub {{ font-size: clamp(1.1rem, 2vw, 1.3rem); color: var(--text-secondary);
      max-width: 640px; margin: 0 auto 3rem; line-height: 1.7; position: relative; z-index: 1; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }}gin: 0 auto 2.5rem; }}

    /* ── Search ── */
    .search-wrap {{ max-width: 640px; margin: 0 auto 1.5rem; position: relative; }}
    .search-input {{ width: 100%; padding: 1rem 1.25rem 1rem 3rem;
      background: var(--bg-card); border: 1px solid var(--border-bright);
      border-radius: var(--radius); color: var(--text-primary); font-size: 1rem;
      font-family: inherit; outline: none; transition: border-color 0.2s, box-shadow 0.2s; }}
    .search-input::placeholder {{ color: var(--text-muted); }}
    .search-input:focus {{ border-color: var(--accent-blue);
      box-shadow: 0 0 0 3px rgba(91,138,245,0.15); }}
    .search-icon {{ position: absolute; left: 1rem; top: 50%; transform: translateY(-50%);
      color: var(--text-muted); font-size: 1.1rem; pointer-events: none; }}

    /* ── Stats ── */
    .stats-bar {{ display: flex; justify-content: center; flex-wrap: wrap; gap: 1.5rem 2.5rem;
      margin-top: 1.5rem; }}
    .stat {{ text-align: center; }}
    .stat-num {{ font-size: 1.75rem; font-weight: 800; font-family: var(--font-mono);
      background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
    .stat-label {{ font-size: 0.75rem; color: var(--text-muted); margin-top: 0.1rem; }}

    /* ── Filters ── */
    .filters {{ max-width: 1400px; margin: 2rem auto 1rem; padding: 0 1.5rem;
      display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center; }}
    .filter-label {{ font-size: 0.75rem; font-weight: 600; color: var(--text-muted);
      text-transform: uppercase; letter-spacing: 0.08em; }}
    .filter-group {{ display: flex; gap: 0.4rem; flex-wrap: wrap; }}
    .filter-btn {{ background: var(--bg-card); border: 1px solid var(--border);
      color: var(--text-secondary); padding: 0.35rem 0.8rem; border-radius: 999px;
      font-size: 0.8rem; cursor: pointer; transition: all 0.15s; font-family: inherit; }}
    .filter-btn:hover {{ border-color: var(--accent-blue); color: var(--text-primary); }}
    .filter-btn.active {{ background: rgba(91,138,245,0.15); border-color: var(--accent-blue);
      color: var(--accent-blue); font-weight: 600; }}
    .sort-select {{ background: var(--bg-card); border: 1px solid var(--border);
      color: var(--text-primary); padding: 0.375rem 0.75rem; border-radius: var(--radius-sm);
      font-size: 0.8rem; cursor: pointer; font-family: inherit; outline: none; }}
    .results-count {{ margin-left: auto; font-size: 0.8rem; color: var(--text-muted); }}

    /* ── Table (Glassmorphism & Physics) ── */
    .table-wrap {{ max-width: 1400px; margin: 0 auto; padding: 0 1.5rem 4rem; }}
    .data-table {{ width: 100%; border-collapse: separate; border-spacing: 0; font-size: 0.875rem; }}
    .data-table thead {{ position: sticky; top: 60px; z-index: 10; }}
    .data-table th {{ background: rgba(5,5,8,0.9); backdrop-filter: blur(8px);
      border-bottom: 2px solid var(--border-bright);
      padding: 1rem; text-align: left; font-size: 0.75rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-secondary);
      cursor: pointer; white-space: nowrap; user-select: none; transition: color 0.2s; }}
    .data-table th:hover {{ color: var(--text-primary); }}
    .data-table th .sort-arrow {{ margin-left: 0.25rem; opacity: 0.4; }}
    .data-table th.sorted .sort-arrow {{ opacity: 1; color: var(--accent-blue); }}
    .data-table td {{ padding: 1rem; border-bottom: 1px solid var(--border);
      vertical-align: middle; white-space: nowrap; transition: background 0.3s; }}
    
    .hover-row {{ transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; }}
    .hover-row:hover {{ transform: scale(1.01) translateY(-2px); box-shadow: var(--shadow-card), var(--shadow-neon); background: var(--bg-card-hover); z-index: 2; position: relative; border-radius: var(--radius-sm); border: 1px solid var(--border-bright); }}
    .hover-row td {{ transition: border-color 0.3s; }}
    .hover-row:hover td {{ border-bottom-color: transparent; }}

    .model-name {{ font-weight: 700; color: var(--text-primary); font-size: 0.95rem; letter-spacing: -0.01em; }}
    .provider-tag {{ font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; margin-top: 0.2rem; }}
    .price-val {{ font-family: var(--font-mono); font-weight: 600;
      color: var(--accent-green); font-size: 0.85rem; text-shadow: 0 0 10px rgba(78,255,176,0.2); }}
    .price-na {{ color: var(--text-muted); font-size: 0.8rem; font-style: italic; }}
    .elo-val {{ font-family: var(--font-mono); color: var(--accent-blue); font-size: 0.9rem; font-weight: 600; text-shadow: 0 0 10px rgba(109,158,250,0.2); }}
    .tier-badge {{ display: inline-block; padding: 0.2rem 0.5rem; border-radius: 4px;
      font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; }}
    .tier-budget {{ background: rgba(62,255,160,0.15); color: var(--accent-green); }}
    .tier-standard {{ background: rgba(91,138,245,0.15); color: var(--accent-blue); }}
    .tier-mid {{ background: rgba(155,89,245,0.15); color: var(--accent-purple); }}
    .tier-premium {{ background: rgba(255,159,67,0.15); color: var(--accent-orange); }}
    .oss-badge {{ font-size: 0.75rem; }}
    .ctx-val {{ font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-secondary); }}

    /* ── Best Deal Banner ── */
    .best-deal {{ max-width: 1400px; margin: 0 auto 0; padding: 1rem 1.5rem 0; }}
    .best-deal-inner {{ background: linear-gradient(135deg, rgba(62,255,160,0.08), rgba(91,138,245,0.06));
      border: 1px solid rgba(62,255,160,0.2); border-radius: var(--radius);
      padding: 1rem 1.5rem; display: flex; align-items: center; justify-content: space-between;
      flex-wrap: wrap; gap: 0.75rem; }}
    .best-deal-inner span {{ font-size: 0.875rem; }}
    .best-deal-inner strong {{ color: var(--accent-green); }}
    .best-deal-link {{ background: var(--accent-green); color: #000; font-weight: 700;
      font-size: 0.8rem; padding: 0.5rem 1.25rem; border-radius: var(--radius-sm);
      text-decoration: none; transition: opacity 0.2s; }}
    .best-deal-link:hover {{ opacity: 0.85; }}

    /* ── Empty State ── */
    .empty-state {{ text-align: center; padding: 4rem 1rem; color: var(--text-muted); }}
    .empty-state h3 {{ font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--text-secondary); }}

    /* ── Footer ── */
    footer {{ border-top: 1px solid var(--border); padding: 2rem 1.5rem;
      text-align: center; color: var(--text-muted); font-size: 0.8rem; }}
    footer a {{ color: var(--text-secondary); text-decoration: none; }}
    footer a:hover {{ color: var(--text-primary); }}

    /* ── Responsive ── */
    @media (max-width: 768px) {{
      .hero {{ padding: 3rem 1rem 2.5rem; }}
      .data-table td:nth-child(5), .data-table th:nth-child(5),
      .data-table td:nth-child(6), .data-table th:nth-child(6),
      .data-table td:nth-child(7), .data-table th:nth-child(7) {{ display: none; }}
    }}
  </style>
</head>
<body>

<nav>
  <div class="nav-inner">
    <a href="/" class="nav-logo">⚡ LLMCosts.dev</a>
    <div class="nav-links">
      <a href="/compare">Compare <span class="nav-badge">NEW</span></a>
      <a href="/configs">Free Configs</a>
      <a href="/daily-report">Market Report</a>
      <a href="{AFFILIATE_BASE}" target="_blank" rel="noopener"
         style="background:var(--accent-blue);color:#fff;padding:0.4rem 0.9rem;border-radius:6px;font-weight:600;font-size:0.8rem;">
        Get API Key ->
      </a>
    </div>
  </div>
</nav>

<div class="hero">
  <div class="hero-badge">
    <div class="pulse"></div>
    Live Pricing · {total} Models · Updated {today}
  </div>
  <h1>Compare <span class="gradient">LLM API Pricing</span><br>For Every Model in 2026</h1>
  <p class="hero-sub">
    Real-time input &amp; output token costs, benchmark scores, and context windows
    for {total}+ AI models — cross-verified from OpenRouter &amp; LiteLLM daily.
  </p>
  <div class="search-wrap">
    <span class="search-icon">🔍</span>
    <input type="text" id="search" class="search-input" 
           placeholder="Search models, providers, or capabilities (e.g. GPT-4, vision, coding)..."
           autocomplete="off" spellcheck="false">
  </div>
  <div class="stats-bar">
    <div class="stat"><div class="stat-num">{total}</div><div class="stat-label">Total Models</div></div>
    <div class="stat"><div class="stat-num">{providers}</div><div class="stat-label">Providers</div></div>
    <div class="stat"><div class="stat-num">{oss_count}</div><div class="stat-label">Open Source</div></div>
    <div class="stat"><div class="stat-num">{cheapest_price}</div><div class="stat-label">Lowest Input/1M</div></div>
  </div>
</div>

<div class="best-deal" id="best-deal-banner">
  <div class="best-deal-inner">
    <span>🏆 Today's Best Value: <strong>{cheapest_name}</strong> at <strong>{cheapest_price}/1M tokens</strong></span>
    <a href="/models/{cheapest_slug}" class="best-deal-link">View Model -></a>
  </div>
</div>

<div class="filters" id="filters">
  <span class="filter-label">Filter:</span>
  <div class="filter-group" id="tier-filters">
    <button class="filter-btn active" data-tier="" onclick="setTierFilter('')">All Tiers</button>
    <button class="filter-btn" data-tier="budget" onclick="setTierFilter('budget')">Budget</button>
    <button class="filter-btn" data-tier="standard" onclick="setTierFilter('standard')">Standard</button>
    <button class="filter-btn" data-tier="mid" onclick="setTierFilter('mid')">Mid</button>
    <button class="filter-btn" data-tier="premium" onclick="setTierFilter('premium')">Premium</button>
  </div>
  <button class="filter-btn" id="oss-filter" onclick="toggleOSS()">Open Source Only</button>
  <div style="margin-left:auto;display:flex;align-items:center;gap:0.75rem;">
    <span class="filter-label">Sort:</span>
    <select class="sort-select" id="sort-select" onchange="setSort(this.value)">
      <option value="inp_asc">Price: Cheapest First</option>
      <option value="inp_desc">Price: Most Expensive</option>
      <option value="elo_desc">ELO: Highest First</option>
      <option value="name_asc">Name: A–Z</option>
      <option value="ctx_desc">Context: Largest</option>
    </select>
    <span class="results-count" id="results-count">{total} models</span>
  </div>
</div>

<div class="table-wrap">
  <table class="data-table" id="models-table">
    <thead>
      <tr>
        <th>#</th>
        <th>Model</th>
        <th onclick="setSort('inp_asc')">Input/1M <span class="sort-arrow">↕</span></th>
        <th onclick="setSort('out_asc')">Output/1M <span class="sort-arrow">↕</span></th>
        <th onclick="setSort('ctx_desc')">Context <span class="sort-arrow">↕</span></th>
        <th onclick="setSort('elo_desc')">ELO <span class="sort-arrow">↕</span></th>
        <th>Tier</th>
        <th>OSS</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody id="table-body">
      <tr><td colspan="9" style="text-align:center;padding:3rem;color:var(--text-muted)">Loading models…</td></tr>
    </tbody>
  </table>
  <div class="empty-state" id="empty-state" style="display:none">
    <h3>No models found</h3>
    <p>Try a different search term or clear the filters.</p>
  </div>
</div>

<footer>
  <p>
    <a href="/">LLMCosts.dev</a> — Open LLM Pricing Registry |
    Data verified {today} |
    <a href="/llms.txt">llms.txt</a> |
    <a href="/daily-report">Daily Report</a> |
    <a href="/sitemap.xml">Sitemap</a>
  </p>
  <p style="margin-top:0.5rem">
    Prices from OpenRouter &amp; LiteLLM. Found an error?
    <a href="https://github.com/shadow-nexus-in/llmcosts/issues">Submit an issue -></a>
  </p>
</footer>

<script>
const SITE_URL = "{SITE_URL}";
const MODELS = {models_json};

let query = '';
let tierFilter = '';
let ossOnly = false;
let sortKey = 'inp_asc';

function fmt(val) {{
  if (val == null) return '<span class="price-na">N/A</span>';
  return '<span class="price-val">$' + Number(val).toFixed(4) + '</span>';
}}

function fmtCtx(val) {{
  if (!val) return '<span class="price-na">—</span>';
  if (val >= 1000000) return '<span class="ctx-val">' + (val/1000000).toFixed(1) + 'M</span>';
  if (val >= 1000) return '<span class="ctx-val">' + (val/1000).toFixed(0) + 'K</span>';
  return '<span class="ctx-val">' + val + '</span>';
}}

function fmtElo(val) {{
  if (!val) return '<span class="price-na">—</span>';
  return '<span class="elo-val">' + val + '</span>';
}}

function tierBadge(tier) {{
  if (!tier) return '';
  const cls = 'tier-' + tier;
  return '<span class="tier-badge ' + cls + '">' + tier + '</span>';
}}

function filtered() {{
  return MODELS.filter(m => {{
    if (ossOnly && !m.open_source) return false;
    if (tierFilter && m.tier !== tierFilter) return false;
    if (query) {{
      const q = query.toLowerCase();
      const searchable = (m.name + ' ' + m.provider + ' ' + m.id + ' ' + (m.capabilities||[]).join(' ')).toLowerCase();
      if (!searchable.includes(q)) return false;
    }}
    return true;
  }});
}}

function sorted(arr) {{
  return [...arr].sort((a, b) => {{
    switch(sortKey) {{
      case 'inp_asc': return (a.inp ?? 9999) - (b.inp ?? 9999);
      case 'inp_desc': return (b.inp ?? -1) - (a.inp ?? -1);
      case 'out_asc': return (a.out ?? 9999) - (b.out ?? 9999);
      case 'elo_desc': return (b.elo ?? 0) - (a.elo ?? 0);
      case 'name_asc': return (a.name||'').localeCompare(b.name||'');
      case 'ctx_desc': return (b.context ?? 0) - (a.context ?? 0);
      default: return 0;
    }}
  }});
}}

function render() {{
  const data = sorted(filtered());
  const tbody = document.getElementById('table-body');
  const empty = document.getElementById('empty-state');
  document.getElementById('results-count').textContent = data.length + ' models';

  if (data.length === 0) {{
    tbody.innerHTML = '';
    empty.style.display = 'block';
    return;
  }}
  empty.style.display = 'none';

  tbody.innerHTML = data.map((m, i) => `
    <tr class="hover-row glsp-card" onclick="location.href='./models/${{m.slug}}.html'">
      <td style="color:var(--text-muted);font-size:0.75rem">${{i+1}}</td>
      <td>
        <div class="model-name">${{m.name}}</div>
        <div class="provider-tag">${{m.provider}}</div>
      </td>
      <td>${{fmt(m.inp)}}</td>
      <td>${{fmt(m.out)}}</td>
      <td>${{fmtCtx(m.context)}}</td>
      <td>${{fmtElo(m.elo)}}</td>
      <td>${{tierBadge(m.tier)}}</td>
      <td class="oss-badge">${{m.open_source ? '[PASS]' : ''}}</td>
      <td>
        <a href="./models/${{m.slug}}.html" onclick="event.stopPropagation()"
           style="color:var(--accent-blue);font-size:0.75rem;text-decoration:none;">
          Details ->
        </a>
      </td>
    </tr>
  `).join('');
}}

function setTierFilter(t) {{
  tierFilter = t;
  document.querySelectorAll('.filter-btn[data-tier]').forEach(b => {{
    b.classList.toggle('active', b.dataset.tier === t);
  }});
  render();
}}

function toggleOSS() {{
  ossOnly = !ossOnly;
  document.getElementById('oss-filter').classList.toggle('active', ossOnly);
  render();
}}

function setSort(key) {{
  sortKey = key;
  document.getElementById('sort-select').value = key;
  render();
}}

document.getElementById('search').addEventListener('input', e => {{
  query = e.target.value.trim();
  render();
}});

// Initial render
render();
</script>
</body>
</html>"""


def _build_compare_page(models: list[dict]) -> str:
    """Build a side-by-side model comparison tool (pure JS, no backend)."""
    today = time.strftime("%Y-%m-%d")
    models_json = _build_models_json_embed(models)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LLM Model Comparison Tool — Compare Any 2 AI Models | LLMCosts.dev</title>
  <meta name="description" content="Compare any two LLM APIs side-by-side. Pricing, benchmarks, context windows, and cost calculator. Free tool by LLMCosts.dev.">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{SITE_URL}/compare">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --bg-primary: #0a0a0f; --bg-secondary: #111118; --bg-card: #16161f;
      --bg-card-hover: #1d1d2a; --border: #1e1e2e; --border-bright: #2d2d45;
      --text-primary: #e8e8f0; --text-secondary: #8888aa; --text-muted: #555577;
      --accent-blue: #5b8af5; --accent-purple: #9b59f5; --accent-green: #3effa0;
      --accent-orange: #ff9f43; --accent-red: #ff4757;
      --font-mono: 'JetBrains Mono', monospace;
      --radius: 12px; --radius-sm: 8px;
    }}
    body {{ font-family: 'Inter', -apple-system, sans-serif; background: var(--bg-primary);
      color: var(--text-primary); min-height: 100vh; }}
    nav {{ position: sticky; top: 0; z-index: 100; background: rgba(10,10,15,0.92);
      backdrop-filter: blur(20px); border-bottom: 1px solid var(--border); padding: 0 1.5rem; }}
    .nav-inner {{ max-width: 1400px; margin: 0 auto; display: flex; align-items: center;
      justify-content: space-between; height: 60px; }}
    .nav-logo {{ font-size: 1.15rem; font-weight: 700;
      background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-decoration: none; }}
    .nav-links {{ display: flex; gap: 1.5rem; }}
    .nav-links a {{ color: var(--text-secondary); text-decoration: none; font-size: 0.875rem; }}
    .nav-links a:hover {{ color: var(--text-primary); }}
    .hero {{ background: linear-gradient(135deg, #111118 0%, #161627 100%);
      padding: 3rem 1.5rem 2.5rem; border-bottom: 1px solid var(--border); text-align: center; }}
    h1 {{ font-size: clamp(1.75rem, 4vw, 2.75rem); font-weight: 700; margin-bottom: 0.75rem; }}
    h1 span {{ background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
    .hero-sub {{ color: var(--text-secondary); font-size: 1rem; }}

    .page-body {{ max-width: 1200px; margin: 0 auto; padding: 2rem 1.5rem 4rem; }}

    /* ── Pickers ── */
    .picker-row {{ display: grid; grid-template-columns: 1fr auto 1fr; gap: 1.5rem;
      align-items: start; margin-bottom: 2rem; }}
    .vs-badge {{ display: flex; align-items: center; justify-content: center;
      font-size: 1.25rem; font-weight: 800; color: var(--text-muted);
      padding-top: 2rem; }}
    .picker-box {{ background: var(--bg-card); border: 1px solid var(--border);
      border-radius: var(--radius); padding: 1.5rem; }}
    .picker-label {{ font-size: 0.7rem; font-weight: 600; text-transform: uppercase;
      letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 0.75rem; }}
    .picker-search {{ width: 100%; padding: 0.75rem 1rem;
      background: var(--bg-secondary); border: 1px solid var(--border-bright);
      border-radius: var(--radius-sm); color: var(--text-primary); font-size: 0.9rem;
      font-family: inherit; outline: none; margin-bottom: 0.5rem; }}
    .picker-search:focus {{ border-color: var(--accent-blue); }}
    .picker-list {{ max-height: 200px; overflow-y: auto; border: 1px solid var(--border);
      border-radius: var(--radius-sm); }}
    .picker-item {{ padding: 0.6rem 1rem; cursor: pointer; font-size: 0.875rem;
      border-bottom: 1px solid var(--border); transition: background 0.1s; }}
    .picker-item:last-child {{ border-bottom: none; }}
    .picker-item:hover {{ background: var(--bg-card-hover); }}
    .picker-item.selected {{ background: rgba(91,138,245,0.15); color: var(--accent-blue); font-weight: 600; }}
    .picker-item-sub {{ font-size: 0.7rem; color: var(--text-muted); }}

    /* ── Comparison Table ── */
    .compare-table {{ width: 100%; border-collapse: collapse; font-size: 0.9rem; }}
    .compare-table th {{ padding: 1rem 1.25rem; text-align: left;
      background: var(--bg-secondary); border-bottom: 1px solid var(--border-bright);
      font-weight: 600; font-size: 0.8rem; }}
    .compare-table th.model-col {{ text-align: center; }}
    .compare-table td {{ padding: 0.875rem 1.25rem; border-bottom: 1px solid var(--border);
      vertical-align: middle; }}
    .compare-table td.center {{ text-align: center; }}
    .compare-table tr:last-child td {{ border-bottom: none; }}
    .compare-table tr:hover td {{ background: var(--bg-card-hover); }}
    .row-label {{ color: var(--text-muted); font-size: 0.8rem; font-weight: 500; }}
    .val-mono {{ font-family: var(--font-mono); font-size: 0.9rem; }}
    .val-green {{ color: var(--accent-green); }}
    .val-blue {{ color: var(--accent-blue); }}
    .val-better {{ background: rgba(62,255,160,0.08); }}
    .val-worse {{ background: rgba(255,71,87,0.05); }}
    .placeholder-msg {{ text-align: center; padding: 3rem; color: var(--text-muted); font-size: 0.9rem; }}

    /* ── Cost Calculator ── */
    .calc-card {{ background: var(--bg-card); border: 1px solid var(--border);
      border-radius: var(--radius); padding: 1.75rem; margin-top: 2rem; }}
    .calc-title {{ font-size: 0.7rem; font-weight: 600; text-transform: uppercase;
      letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 1.25rem; }}
    .calc-row {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem;
      align-items: center; margin-bottom: 1rem; }}
    .calc-label {{ font-size: 0.85rem; color: var(--text-secondary); }}
    .calc-input {{ width: 100%; padding: 0.625rem 0.875rem;
      background: var(--bg-secondary); border: 1px solid var(--border);
      border-radius: var(--radius-sm); color: var(--text-primary);
      font-family: var(--font-mono); font-size: 0.9rem; outline: none; }}
    .calc-input:focus {{ border-color: var(--accent-blue); }}
    .calc-results {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1.5rem; }}
    .calc-result-card {{ background: var(--bg-secondary); border: 1px solid var(--border);
      border-radius: var(--radius-sm); padding: 1rem; text-align: center; }}
    .calc-model-name {{ font-size: 0.75rem; color: var(--text-muted); margin-bottom: 0.25rem; }}
    .calc-cost {{ font-size: 1.5rem; font-weight: 700; font-family: var(--font-mono);
      color: var(--accent-green); }}
    .calc-savings {{ text-align: center; margin-top: 1rem; font-size: 0.875rem; color: var(--text-secondary); }}
    .calc-savings strong {{ color: var(--accent-green); }}

    footer {{ border-top: 1px solid var(--border); padding: 2rem 1.5rem;
      text-align: center; color: var(--text-muted); font-size: 0.8rem; }}
    footer a {{ color: var(--text-secondary); text-decoration: none; }}
    @media (max-width: 768px) {{
      .picker-row {{ grid-template-columns: 1fr; }}
      .vs-badge {{ display: none; }}
      .calc-row {{ grid-template-columns: 1fr; }}
      .calc-results {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>

<nav>
  <div class="nav-inner">
    <a href="/" class="nav-logo">⚡ LLMCosts.dev</a>
    <div class="nav-links">
      <a href="/">All Models</a>
      <a href="/configs">Configs</a>
      <a href="/daily-report">Market Report</a>
    </div>
  </div>
</nav>

<div class="hero">
  <h1>LLM Model <span>Comparison Tool</span></h1>
  <p class="hero-sub">Pick any two models and compare pricing, benchmarks, and cost at scale · {today}</p>
</div>

<div class="page-body">
  <div class="picker-row">
    <div class="picker-box">
      <div class="picker-label">Model A</div>
      <input type="text" id="search-a" class="picker-search" placeholder="Search models…" oninput="filterList('a')">
      <div class="picker-list" id="list-a"></div>
    </div>
    <div class="vs-badge">VS</div>
    <div class="picker-box">
      <div class="picker-label">Model B</div>
      <input type="text" id="search-b" class="picker-search" placeholder="Search models…" oninput="filterList('b')">
      <div class="picker-list" id="list-b"></div>
    </div>
  </div>

  <div id="compare-area">
    <p class="placeholder-msg">👆 Select two models above to compare them side-by-side.</p>
  </div>

  <div class="calc-card" id="calc-card" style="display:none">
    <div class="calc-title">💰 Cost Calculator — Estimate Your Monthly Bill</div>
    <div class="calc-row">
      <div>
        <div class="calc-label">API Calls / Month</div>
        <input type="number" id="calc-calls" class="calc-input" value="100000" oninput="calcCost()">
      </div>
      <div>
        <div class="calc-label">Avg Input Tokens / Call</div>
        <input type="number" id="calc-in" class="calc-input" value="500" oninput="calcCost()">
      </div>
      <div>
        <div class="calc-label">Avg Output Tokens / Call</div>
        <input type="number" id="calc-out" class="calc-input" value="200" oninput="calcCost()">
      </div>
    </div>
    <div class="calc-results">
      <div class="calc-result-card">
        <div class="calc-model-name" id="calc-name-a">Model A</div>
        <div class="calc-cost" id="calc-cost-a">$0.00</div>
        <div style="font-size:0.7rem;color:var(--text-muted);margin-top:0.25rem">per month</div>
      </div>
      <div class="calc-result-card">
        <div class="calc-model-name" id="calc-name-b">Model B</div>
        <div class="calc-cost" id="calc-cost-b">$0.00</div>
        <div style="font-size:0.7rem;color:var(--text-muted);margin-top:0.25rem">per month</div>
      </div>
    </div>
    <div class="calc-savings" id="calc-savings"></div>
  </div>
</div>

<footer>
  <p>
    <a href="{SITE_URL}">LLMCosts.dev</a> — Open LLM Pricing Registry |
    Data verified {today}
  </p>
</footer>

<script>
const SITE_URL = "{SITE_URL}";
const MODELS = {models_json};

let selA = null, selB = null;

function filterList(side) {{
  const q = document.getElementById('search-' + side).value.toLowerCase();
  const matches = MODELS.filter(m => {{
    const s = (m.name + ' ' + m.provider + ' ' + m.id).toLowerCase();
    return !q || s.includes(q);
  }}).slice(0, 30);

  const el = document.getElementById('list-' + side);
  const current = side === 'a' ? selA : selB;
  el.innerHTML = matches.map(m => `
    <div class="picker-item ${{current && current.id === m.id ? 'selected' : ''}}"
         onclick="select('${{side}}', '${{m.id}}')">
      ${{m.name}}
      <div class="picker-item-sub">${{m.provider}} · ${{m.inp != null ? '$' + m.inp.toFixed(4) + '/1M in' : 'price N/A'}}</div>
    </div>
  `).join('');
}}

function select(side, id) {{
  const m = MODELS.find(x => x.id === id);
  if (!m) return;
  if (side === 'a') selA = m;
  else selB = m;
  filterList(side);
  renderCompare();
}}

function fmt(val) {{
  if (val == null) return '<span style="color:var(--text-muted)">N/A</span>';
  return '$' + Number(val).toFixed(4);
}}

function renderCompare() {{
  const area = document.getElementById('compare-area');
  const calcCard = document.getElementById('calc-card');
  if (!selA || !selB) {{
    area.innerHTML = '<p class="placeholder-msg">👆 Select two models to compare.</p>';
    calcCard.style.display = 'none';
    return;
  }}
  calcCard.style.display = 'block';

  const rows = [
    ['Input Price/1M', fmt(selA.inp), fmt(selB.inp), 'inp', 'lower'],
    ['Output Price/1M', fmt(selA.out), fmt(selB.out), 'out', 'lower'],
    ['Cached Input/1M', fmt(selA.cached), fmt(selB.cached), 'cached', 'lower'],
    ['Context Window', fmtCtx(selA.context), fmtCtx(selB.context), 'context', 'higher'],
    ['LMSYS Arena ELO', selA.elo || 'N/A', selB.elo || 'N/A', 'elo', 'higher'],
    ['MMLU Score', selA.mmlu || 'N/A', selB.mmlu || 'N/A', 'mmlu', 'higher'],
    ['Tier', selA.tier || 'N/A', selB.tier || 'N/A', null, null],
    ['Open Source', selA.open_source ? '[PASS] Yes' : '[FAIL] No', selB.open_source ? '[PASS] Yes' : '[FAIL] No', null, null],
  ];

  function cellClass(field, prefer, aVal, bVal) {{
    if (!field || !prefer) return '';
    const a = parseFloat(aVal), b = parseFloat(bVal);
    if (isNaN(a) || isNaN(b)) return '';
    const aBetter = prefer === 'lower' ? a < b : a > b;
    const bBetter = prefer === 'lower' ? b < a : b > a;
    return {{ a: aBetter ? 'val-better' : bBetter ? 'val-worse' : '', b: bBetter ? 'val-better' : aBetter ? 'val-worse' : '' }};
  }}

  area.innerHTML = `
    <table class="compare-table">
      <thead>
        <tr>
          <th style="width:200px">Metric</th>
          <th class="model-col">${{selA.name}}<div style="font-size:0.7rem;color:var(--text-muted);font-weight:400">${{selA.provider}}</div></th>
          <th class="model-col">${{selB.name}}<div style="font-size:0.7rem;color:var(--text-muted);font-weight:400">${{selB.provider}}</div></th>
        </tr>
      </thead>
      <tbody>
        ${{rows.map(([label, a, b, field, prefer]) => {{
          const cls = prefer ? cellClass(field, prefer, selA[field], selB[field]) : {{a:'',b:''}};
          return `<tr>
            <td class="row-label">${{label}}</td>
            <td class="center ${{cls.a}}">${{a}}</td>
            <td class="center ${{cls.b}}">${{b}}</td>
          </tr>`;
        }}).join('')}}
        <tr>
          <td class="row-label">View Details</td>
          <td class="center"><a href="./models/${{selA.slug}}.html" style="color:var(--accent-blue);font-size:0.875rem;">Details -></a></td>
          <td class="center"><a href="./models/${{selB.slug}}.html" style="color:var(--accent-blue);font-size:0.875rem;">Details -></a></td>
        </tr>
      </tbody>
    </table>
  `;

  document.getElementById('calc-name-a').textContent = selA.name;
  document.getElementById('calc-name-b').textContent = selB.name;
  calcCost();
}}

function fmtCtx(val) {{
  if (!val) return 'N/A';
  if (val >= 1000000) return (val/1000000).toFixed(1) + 'M';
  if (val >= 1000) return (val/1000).toFixed(0) + 'K';
  return val;
}}

function calcCost() {{
  if (!selA || !selB) return;
  const calls = parseInt(document.getElementById('calc-calls').value) || 0;
  const inTok = parseInt(document.getElementById('calc-in').value) || 0;
  const outTok = parseInt(document.getElementById('calc-out').value) || 0;

  function cost(m) {{
    const inp = (m.inp || 0) * inTok * calls / 1_000_000;
    const out2 = (m.out || 0) * outTok * calls / 1_000_000;
    return inp + out2;
  }}

  const ca = cost(selA), cb = cost(selB);
  document.getElementById('calc-cost-a').textContent = '$' + ca.toFixed(2);
  document.getElementById('calc-cost-b').textContent = '$' + cb.toFixed(2);

  const diff = Math.abs(ca - cb);
  const cheaper = ca < cb ? selA.name : selB.name;
  const pct = Math.max(ca, cb) > 0 ? ((diff / Math.max(ca, cb)) * 100).toFixed(1) : 0;

  if (diff > 0.01) {{
    document.getElementById('calc-savings').innerHTML =
      `<strong>${{cheaper}}</strong> is <strong>${{pct}}% cheaper</strong> — saving <strong>$${{diff.toFixed(2)}}/month</strong>`;
  }} else {{
    document.getElementById('calc-savings').textContent = 'Both models cost approximately the same.';
  }}
}}

// Init pickers with all models
filterList('a');
filterList('b');
</script>
</body>
</html>"""


def run_homepage_generation() -> dict:
    """Main entry point. Generates homepage + compare page."""
    summary = {"files_written": 0, "errors": 0}

    logger.info("=" * 60)
    logger.info("HOMEPAGE GENERATOR: Building index + compare pages...")

    models = _load_models()
    if not models:
        summary["errors"] += 1
        return summary

    try:
        homepage = _build_homepage(models)
        _atomic_write(DIST_DIR / "index.html", homepage)
        summary["files_written"] += 1
        logger.info("  [PASS] dist/index.html")

        compare = _build_compare_page(models)
        _atomic_write(DIST_DIR / "compare" / "index.html", compare)
        summary["files_written"] += 1
        logger.info("  [PASS] dist/compare/index.html")
    except Exception as e:
        logger.error(f"Homepage generation failed: {e}", exc_info=True)
        summary["errors"] += 1

    logger.info(f"Homepage generation complete: {summary}")
    return summary
