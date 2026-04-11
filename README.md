# ⚡ LLMCosts.dev — The Open LLM Pricing Registry

[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-LLM_Cost_Optimizer-brightgreen?logo=github)](https://github.com/marketplace/actions/llm-cost-optimizer)
[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-yellow)](https://huggingface.co/spaces/DIVYAPRATAP07/llm-cost-optimizer-dev)
[![Deployed on Cloudflare](https://img.shields.io/badge/Deployed-Cloudflare_Pages-orange)](https://llmcosts.dev)

LLMCosts.dev is a completely automated, zero-maintenance, zero-database architecture that powers an open registry of LLM API pricing, benchmark data, and arbitrage intelligence.

This repository natively generates a high-performance static website, B2B market reports, and heavily optimized developer configurations (LiteLLM, Cursor, OpenRouter), hosting them across a multi-platform "SEO Parasite" ecosystem for maximum reach and zero operational cost.

---

## 📍 Deployment Ecosystem

The project is natively registered and synchronized across three high-authority platforms to ensure 100% uptime and #1 search visibility:

*   **Primary Dashboard**: [llmcosts.dev](https://llmcosts.dev) (High-speed Cloudflare Edge)
*   **Hugging Face "SEO Hijack"**: [DIVYAPRATAP07/llm-cost-optimizer-dev](https://huggingface.co/spaces/DIVYAPRATAP07/llm-cost-optimizer-dev) (Ranked on Hugging Face for instant Google authority)
*   **GitHub Marketplace**: [LLM Cost Optimizer Action](https://github.com/marketplace/actions/llm-cost-optimizer) (Automated CI/CD supply-chain integration)

---

## 🏗️ The "Zen Godmode V9" Architecture

Unlike traditional web applications that suffer from database bottlenecks and bloat, LLMCosts is built on a mathematically proven static ingestion model:

1.  **Single Source of Truth**: Data resides in `data/models.json` (no SQL/NoSQL required).
2.  **Autonomous Build Engine**: An indestructible Python orchestrator (`build.py`) running daily via GitHub Actions.
3.  **Multi-Target Deployment**: Pure HTML/JS output is pushed simultaneously to Cloudflare, GitHub Pages, and Hugging Face.
4.  **DR 90+ Parasite Syndication**: Auto-publishes AI-generated VS Showdown articles to Dev.to (DR 93) via API for instant Google ranking.

## 🌟 Key Features

*   **Continuous Autonomous Updates**: Fetches exact pricing matrices daily from OpenRouter and LiteLLM with dual-source cross-validation.
*   **Mega-Page Generator**: Leverages surplus Groq API keys to autonomously write 300+ hyper-detailed model comparison pages with 25 FAQs and Schema.org JSON-LD.
*   **VS Showdown Engine**: Auto-generates head-to-head comparison pages for the Top 50 models with Groq Llama-3 analysis.
*   **The Mega-Configs**: Auto-generates exact routing fallback chains and optimized `.yaml` files specifically to guarantee the absolute lowest cost per token.
*   **Machine-First SEO (`llms.txt`)**: Natively shards the registry into structured Markdown ensuring #1 crawler ingestion by Perplexity, Claude, and ChatGPT. Includes industry-standard `CitationTemplate` for guaranteed AI attribution.
*   **Dev.to Parasite Pipeline**: Autonomous syndication engine publishes CTO-grade technical articles to Dev.to (DR 93), complete with canonical backlinks to the main domain for SEO authority transfer.
*   **Auto-Ingestor (V9)**: Discovers and ingests new models from OpenRouter automatically, using Groq AI to classify capabilities, tier, and use-cases — zero human intervention.
*   **PR Infiltrator Bot**: Submits upstream PRs to high-authority open-source repos with registry data to generate high-quality backlinks.

---

## 📁 Repository Structure

```text
llmcosts/
├── build.py                  # The Godmode Orchestrator (Entry Point)
├── data/
│   └── models.json           # Single Source of Truth (300+ models)
├── src/
│   ├── core/
│   │   └── groq_client.py    # 4-Key Round-Robin Groq Engine
│   ├── generators/
│   │   ├── homepage.py       # Homepage + Compare Tool Generator
│   │   ├── model_pages.py    # 300+ Mega-Page Generator (HTML + MD)
│   │   ├── vs_generator.py   # VS Showdown Engine (Top 50)
│   │   ├── llms_txt.py       # AI Citation Shards (llms.txt protocol)
│   │   ├── dev_configs.py    # LiteLLM/Cursor/OpenRouter Configs
│   │   ├── market_report.py  # Daily Intelligence Report
│   │   └── sitemap.py        # Sitemap + Google Indexing API
│   └── automation/
│       ├── auto_ingestor.py  # OpenRouter Auto-Discovery + Groq AI
│       ├── price_updater.py  # Dual-Source Live Price Sync
│       ├── pr_bot.py         # GitHub PR Backlink Infiltrator
│       └── publish_network.py # Dev.to DR93 Parasite Pipeline
├── templates/
│   ├── model_page.html       # Lightning-fast Mega-template
│   └── vs_page.html          # VS Showdown Template
└── dist/                     # The final built website & assets
```

## 🔐 Required Secrets (GitHub Actions)

| Secret | Purpose |
|--------|---------|
| `GROQ_API_KEY_1` through `GROQ_API_KEY_4` | 4-key round-robin Groq AI engine |
| `BOT_GITHUB_PAT` | PR infiltrator authentication |
| `GOOGLE_INDEXING_API_KEY` | Force Google to index new pages |
| `DEVTO_API_KEY` | Dev.to parasite syndication (optional — build never crashes without it) |
| `SITE_URL` | Primary domain (defaults to `https://llmcosts.dev`) |

## 🚀 Getting Started (Local Development)

1.  **Clone & Install**:
    ```bash
    git clone https://github.com/shadow-nexus-in/llmcosts.git
    pip install -r requirements.txt
    ```

2.  **Configure**:
    ```bash
    cp .env.example .env
    # Add your GROQ_API_KEY_1 (minimum)
    ```

3.  **Run the Build**:
    ```bash
    python build.py
    ```

4.  **Preview**:
    Open `dist/index.html` in your browser.

## 🛡️ Reliability Guarantees

- **Full Failure Isolation**: Every task in the orchestrator runs in its own try/except. If one module crashes, all other modules still complete successfully.
- **Atomic File Writes**: All file writes use temp-file-then-rename pattern. The live site is never corrupted by a partial write.
- **Graceful Degradation**: Missing API keys (Groq, Dev.to, Google) cause the relevant module to skip silently — never a pipeline crash.
- **JSON Validation**: All atomic writes to `models.json` validate the JSON output before replacing the live file.

---
*Maintained autonomously by LLMCosts.dev. All inference routed through [OpenRouter](https://openrouter.ai/?ref=llmcosts) is tracking-enabled for infrastructure maintenance.*
