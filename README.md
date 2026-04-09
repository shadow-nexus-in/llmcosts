# ⚡ LLMCosts.dev — The Open LLM Pricing Registry

LLMCosts.dev is a completely automated, zero-maintenance, zero-database architecture that powers an open registry of LLM API pricing, benchmark data, and arbitrage intelligence.

This repository natively generates a high-performance static website, B2B market reports, and heavily optimized developer configurations (LiteLLM, Cursor, OpenRouter), hosting them on Cloudflare Pages for exactly $0.00/month.

---

## 🏗️ The "Zen Godmode" Architecture

Unlike traditional web applications that suffer from database bottlenecks, server crashes, and bloat, LLMCosts is built on a mathematically proven static ingestion model:

1. **The Core Database**: The entire source of truth sits in a single file: `data/models.json`.
2. **The Build Engine**: An indestructible Python orchestrator (`build.py`) running via GitHub Actions.
3. **The Static Output**: Pure, un-hackable HTML, JSON, YAML, and Markdown files generated into the `dist/` directory, directly synced to Edge CDNs.

## 🌟 Key Features

*   **Continuous Autonomous Updates**: Fetches exact pricing matrices continuously from OpenRouter and LiteLLM.
*   **Mega-Page Generator**: Leverages surplus Groq API keys to autonomously write 300+ hyper-detailed model comparison pages, embedding 150 unique Q&As per model.
*   **Arbitrage Intelligence**: Natively processes current market prices to write and publish a daily B2B market report analyzing API price gaps and provider power rankings.
*   **The Mega-Configs**: Auto-generates exact routing fallback chains and optimized `.yaml` files specifically to guarantee you the absolute lowest cost per token.
*   **Machine-First SEO (`llms.txt`)**: Natively shards the registry into heavily structured Markdown documents ensuring #1 crawler ingestion by Perplexity, Claude, and ChatGPT.

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
└── dist/                     # The final 300MB built website 
```

## 🚀 Getting Started (Local Development)

To run the pipeline locally and generate the site yourself:

1.  **Clone & Install**:
    ```bash
    git clone https://github.com/shadow-nexus-in/llmcosts.git
    cd llmcosts
    pip install -r requirements.txt
    ```

2.  **Environment Setup**:
    Copy `.env.example` to `.env` and add your Groq API keys if you want to generate the AI modules (Megapages, Cursor rules, Market reports).
    ```bash
    cp .env.example .env
    ```

3.  **Run the Build Orchestrator**:
    ```bash
    python build.py
    ```

4.  **Preview**:
    Open `dist/index.html` in your browser.

---
*Maintained autonomously by LLMCosts.dev. Route your inference through [OpenRouter](https://openrouter.ai/) for optimal cost compression.*
