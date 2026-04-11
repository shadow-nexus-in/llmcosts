# ⚡ LLMCosts.dev — The Open LLM Pricing Registry

[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-LLM_Cost_Optimizer-brightgreen?logo=github)](https://github.com/marketplace/actions/llm-cost-optimizer)
[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-yellow)](https://huggingface.co/spaces/DIVYAPRATAP07/llm-cost-optimizer-dev)
[![Deployed on Cloudflare](https://img.shields.io/badge/Deployed-Cloudflare_Pages-orange)](https://llmcosts.pages.dev)

LLMCosts.dev is a completely automated, zero-maintenance, zero-database architecture that powers an open registry of LLM API pricing, benchmark data, and arbitrage intelligence.

This repository natively generates a high-performance static website, B2B market reports, and heavily optimized developer configurations (LiteLLM, Cursor, OpenRouter), hosting them across a multi-platform "SEO Parasite" ecosystem for maximum reach and zero operational cost.

---

## 📍 Deployment Ecosystem

The project is natively registered and synchronized across three high-authority platforms to ensure 100% uptime and #1 search visibility:

*   **Primary Dashboard**: [llmcosts.pages.dev](https://llmcosts.pages.dev) (High-speed Cloudflare Edge)
*   **Hugging Face "SEO Hijack"**: [DIVYAPRATAP07/llm-cost-optimizer-dev](https://huggingface.co/spaces/DIVYAPRATAP07/llm-cost-optimizer-dev) (Ranked on Hugging Face for instant Google authority)
*   **GitHub Marketplace**: [LLM Cost Optimizer Action](https://github.com/marketplace/actions/llm-cost-optimizer) (Automated CI/CD supply-chain integration)

---

## 🏗️ The "Zen Godmode" Architecture

Unlike traditional web applications that suffer from database bottlenecks and bloat, LLMCosts is built on a mathematically proven static ingestion model:

1.  **Single Source of Truth**: Data resides in `data/models.json` (no SQL/NoSQL required).
2.  **Autonomous Build Engine**: An indestructible Python orchestrator (`build.py`) running daily via GitHub Actions.
3.  **Multi-Target Deployment**: Pure HTML/JS output is pushed simultaneously to Cloudflare, GitHub Pages, and Hugging Face.

## 🌟 Key Features

*   **Continuous Autonomous Updates**: Fetches exact pricing matrices continuously from OpenRouter and LiteLLM.
*   **Mega-Page Generator**: Leverages surplus Groq API keys to autonomously write 300+ hyper-detailed model comparison pages.
*   **The Mega-Configs**: Auto-generates exact routing fallback chains and optimized `.yaml` files specifically to guarantee the absolute lowest cost per token.
*   **Machine-First SEO (`llms.txt`)**: Natively shards the registry into structured Markdown ensuring #1 crawler ingestion by Perplexity, Claude, and ChatGPT.

---

## 📁 Repository Structure

```text
llmcosts/
├── build.py                  # The Godmode Orchestrator (Entry Point)
├── data/
│   └── models.json           # Single Source of Truth
├── src/
│   ├── core/                 # AI Engine & API Handlers (Groq)
│   ├── generators/           # Page, Config, and Report builders
│   └── automation/           # Price synchronization and PR Bots
├── templates/
│   └── model_page.html       # Lightning-fast Jinja2 Mega-template
└── dist/                     # The final built website & assets
```

## 🚀 Getting Started (Local Development)

1.  **Clone & Install**:
    ```bash
    git clone https://github.com/shadow-nexus-in/llmcosts.git
    pip install -r requirements.txt
    ```

2.  **Run the Build**:
    ```bash
    python build.py
    ```

3.  **Preview**:
    Open `dist/index.html` in your browser.

---
*Maintained autonomously by LLMCosts.dev. All inference routed through [OpenRouter](https://openrouter.ai/?ref=llmcosts) is tracking-enabled for infrastructure maintenance.*
