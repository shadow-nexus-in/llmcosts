#!/usr/bin/env python3
"""
GODMODE V8 — Master Build Orchestrator
The single entry point for the entire LLMCosts.dev pipeline.

Usage:
  python build.py                    # Full build
  python build.py --model gpt-4o    # Test single model
  python build.py --skip-pages      # Skip page generation (prices + llms.txt only)
  python build.py --skip-pr         # Skip PR infiltrator

Each task runs independently. Failure of one NEVER stops others.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path

# ──────────────────────────────────────────────────────────────
# Bootstrap: Load .env if present
# ──────────────────────────────────────────────────────────────
def _load_dotenv() -> None:
    env_file = Path(".env")
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val

_load_dotenv()

# ──────────────────────────────────────────────────────────────
# Logging — beautiful, structured, timestamped
# ──────────────────────────────────────────────────────────────
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"build_{time.strftime('%Y%m%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)
logger = logging.getLogger("build")


# ──────────────────────────────────────────────────────────────
# Task Runner — full failure isolation
# ──────────────────────────────────────────────────────────────
def _run_task(task_name: str, fn, *args, **kwargs) -> dict:
    """
    Runs a task function with full exception isolation.
    Returns the task's summary dict, or an error dict.
    Never raises.
    """
    logger.info(f"\n{'='*60}")
    logger.info(f"TASK START: {task_name}")
    logger.info(f"{'='*60}")
    start = time.monotonic()
    try:
        result = fn(*args, **kwargs) or {}
        elapsed = round(time.monotonic() - start, 2)
        logger.info(f"TASK DONE: {task_name} — {elapsed}s — {result}")
        return {"status": "ok", "elapsed": elapsed, **result}
    except Exception as e:
        elapsed = round(time.monotonic() - start, 2)
        logger.error(f"TASK FAILED: {task_name} — {elapsed}s — {e}", exc_info=True)
        return {"status": "error", "elapsed": elapsed, "error": str(e)}


# ──────────────────────────────────────────────────────────────
# Build Report
# ──────────────────────────────────────────────────────────────
def _write_build_report(results: dict) -> None:
    report = {
        "build_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "tasks": results,
    }
    Path("build_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    logger.info("Build report saved → build_report.json")


# ──────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────
def main() -> int:
    parser = argparse.ArgumentParser(
        description="GODMODE V8 — LLMCosts.dev Build Orchestrator"
    )
    parser.add_argument("--model", help="Build only a single model slug (e.g. gpt-4o)")
    parser.add_argument("--skip-pages", action="store_true", help="Skip HTML/MD page generation")
    parser.add_argument("--skip-prices", action="store_true", help="Skip live price update")
    parser.add_argument("--skip-pr", action="store_true", help="Skip GitHub PR infiltrator")
    parser.add_argument("--skip-configs", action="store_true", help="Skip config file generation")
    args = parser.parse_args()

    build_start = time.monotonic()
    logger.info("🚀 GODMODE V8 BUILD PIPELINE STARTING")
    logger.info(f"   Date: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}")
    logger.info(f"   Log : {LOG_FILE}")

    results = {}

    # ── 0. Homepage + Compare Page ───────────────────────────
    if not args.model:
        from src.generators.homepage import run_homepage_generation
        results["homepage"] = _run_task("Homepage Generator", run_homepage_generation)

    # ── 1. Price Update ──────────────────────────────────────
    if not args.skip_prices:
        from src.automation.price_updater import run_price_update
        results["price_update"] = _run_task("Price Updater", run_price_update)

        from src.automation.auto_ingestor import run_ingestion
        results["auto_ingestor"] = _run_task("Auto Ingestor", run_ingestion)
    else:
        logger.info("Skipping price update (--skip-prices)")
    # ── 2. Page Generation ───────────────────────────────────
    if not args.skip_pages:
        from src.generators.model_pages import run_page_generation
        results["page_generation"] = _run_task(
            "Page Generator",
            run_page_generation,
            single_model=args.model,
        )

        total_files = len(list(Path("dist").glob("**/*.html")))
        if total_files > 19000:
            logger.warning(f"Cloudflare threshold hit ({total_files} files). Skipping Versus Engine.")
        else:
            from src.generators.vs_generator import run_vs_generation
            results["vs_generation"] = _run_task("Versus Engine", run_vs_generation)
    else:
        logger.info("Skipping page generation (--skip-pages)")

    # ── 3. LLMs.txt Sharding ─────────────────────────────────
    from src.generators.llms_txt import run_llms_txt_generation
    results["llms_txt"] = _run_task("LLMs.txt Engine", run_llms_txt_generation)

    # ── 4. Config Generator ──────────────────────────────────
    if not args.skip_configs:
        from src.generators.dev_configs import run_config_generation
        results["config_gen"] = _run_task("Config Generator", run_config_generation)
    else:
        logger.info("Skipping config generation (--skip-configs)")

    # ── 5. Daily Intelligence Report ─────────────────────────
    if not args.model:  # Never run in single-model test mode
        from src.generators.market_report import run_report_generation
        results["report_gen"] = _run_task("Report Generator", run_report_generation)

    # ── 6. Sitemap ───────────────────────────────────────────
    from src.generators.sitemap import run_sitemap_generation
    results["sitemap"] = _run_task("Sitemap Builder", run_sitemap_generation)

    # ── 6.5 404 Fallback Page ────────────────────────────────
    try:
        html_404 = """<!DOCTYPE html>
<html lang="en">
<head>
    <title>404 Not Found - LLMCosts.dev</title>
    <style>
      body { font-family: 'Inter', sans-serif; background: #0a0a0f; color: #e8e8f0; text-align: center; padding-top: 100px; }
      a { color: #5b8af5; text-decoration: none; }
      a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>This model page is currently being generated by the AI, or it does not exist.</p>
    <p><a href="/">← Return to Homepage</a></p>
</body>
</html>"""
        Path("dist/404.html").write_text(html_404, encoding="utf-8")
        logger.info("  ✅ dist/404.html fallback generated")
    except Exception as e:
        logger.error(f"Failed to write 404.html: {e}")

    # ── 7. PR Infiltrator ────────────────────────────────────
    if not args.skip_pr and not args.model:  # Never run PR bot in single-model mode
        from src.automation.pr_bot import run_pr_infiltrator
        results["pr_bot"] = _run_task("PR Infiltrator", run_pr_infiltrator)
    else:
        logger.info("Skipping PR infiltrator (--skip-pr or single-model mode)")

    # ── Build Summary ────────────────────────────────────────
    total_elapsed = round(time.monotonic() - build_start, 2)
    errors = sum(1 for r in results.values() if r.get("status") == "error")
    ok = len(results) - errors

    logger.info(f"\n{'='*60}")
    logger.info(f"BUILD COMPLETE — {total_elapsed}s")
    logger.info(f"  Tasks OK   : {ok}")
    logger.info(f"  Tasks FAIL : {errors}")
    logger.info(f"{'='*60}")

    _write_build_report(results)

    # Exit code 0 even with partial failures — site is never broken
    return 0


if __name__ == "__main__":
    sys.exit(main())
