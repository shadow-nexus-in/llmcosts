"""Full system audit script - checks every logic path for errors."""
import json
import os
import re

print("=" * 70)
print("GODMODE FULL SYSTEM AUDIT - PASS 1")
print("=" * 70)

errors = []

# ----- 1. models.json structure -----
d = json.load(open("data/models.json", encoding="utf-8"))
if not isinstance(d, dict):
    errors.append("BUG: models.json root is not a dict")
if "models" not in d:
    errors.append("BUG: models.json missing models key")
models = d.get("models", [])
for i, m in enumerate(models):
    if not m.get("id"):
        errors.append(f"BUG: model at index {i} has no id")
    if not m.get("slug"):
        errors.append(f"BUG: model {m.get('id','?')} has no slug")
    if m.get("pricing") is None:
        errors.append(f"BUG: model {m['id']} pricing is None")

# ----- 2. dev_configs SITE_URL hardcoded -----
with open("src/generators/dev_configs.py", encoding="utf-8") as f:
    dc = f.read()
    if 'SITE_URL = "https://llmcosts.dev"' in dc and "os.getenv" not in dc:
        errors.append("BUG: dev_configs.py SITE_URL is hardcoded, not from os.getenv")

# ----- 3. publish_network.py data['models'] fix verified -----
with open("src/automation/publish_network.py", encoding="utf-8") as f:
    pn = f.read()
    if "for m in data:" in pn:
        errors.append("BUG: publish_network.py still iterates root dict")
    if "dirname(__name__)" in pn:
        errors.append("BUG: publish_network.py still uses __name__ instead of __file__")

# ----- 4. llms_txt.py citation domain check -----
with open("src/generators/llms_txt.py", encoding="utf-8") as f:
    lt = f.read()
    if "llmcosts.pages.dev" in lt:
        errors.append("BUG: llms_txt.py still references the internal Cloudflare domain")
    if "CitationTemplate" not in lt:
        errors.append("BUG: llms_txt.py missing CitationTemplate")
    if "os.getenv" not in lt:
        errors.append("BUG: llms_txt.py SITE_URL not from os.getenv")

# ----- 5. groq_client.py get_groq_client exists -----
with open("src/core/groq_client.py", encoding="utf-8") as f:
    gc = f.read()
    if "def get_groq_client" not in gc:
        errors.append("BUG: groq_client.py missing get_groq_client factory function")

# ----- 6. vs_generator.py bare except -----
with open("src/generators/vs_generator.py", encoding="utf-8") as f:
    vg = f.read()
    bare_except_count = len(re.findall(r"except\s*:", vg))
    if bare_except_count > 0:
        errors.append(f"WARN: vs_generator.py has {bare_except_count} bare except(s) (anti-pattern)")

# ----- 7. sitemap.py model ID guard -----
with open("src/generators/sitemap.py", encoding="utf-8") as f:
    sm = f.read()
    if "if not mid:" not in sm:
        errors.append("BUG: sitemap.py missing ID guard in URL generation loop")

# ----- 8. market_report model loading -----
with open("src/generators/market_report.py", encoding="utf-8") as f:
    mr = f.read()
    if "models" not in mr:
        errors.append("BUG: market_report.py may not load models correctly")
    # Check for data.get("models") pattern
    has_models_key = ('data.get("models"' in mr or "data.get('models'" in mr)
    if not has_models_key:
        errors.append("BUG: market_report.py does not use data.get('models') pattern")

# ----- 9. daily_build.yml DEVTO_API_KEY present -----
with open(".github/workflows/daily_build.yml", encoding="utf-8") as f:
    yml = f.read()
    if "DEVTO_API_KEY" not in yml:
        errors.append("BUG: daily_build.yml missing DEVTO_API_KEY secret injection")
    if "publish_network" not in yml:
        errors.append("BUG: daily_build.yml missing publish_network.py execution step")

# ----- 10. homepage.py SITE_URL from env -----
with open("src/generators/homepage.py", encoding="utf-8") as f:
    hp = f.read()
    if "os.getenv" not in hp:
        errors.append("BUG: homepage.py does not read SITE_URL from environment")

# ----- 11. pr_bot model ID guard -----
with open("src/automation/pr_bot.py", encoding="utf-8") as f:
    pr = f.read()
    if "if m.get" not in pr:
        errors.append("BUG: pr_bot.py missing model ID guard")

# ----- 12. model_pages SITE_URL from env -----
with open("src/generators/model_pages.py", encoding="utf-8") as f:
    mp = f.read()
    if "os.getenv" not in mp:
        errors.append("BUG: model_pages.py does not read SITE_URL from environment")

# ----- 13. auto_ingestor _atomic_write validates JSON -----
with open("src/automation/auto_ingestor.py", encoding="utf-8") as f:
    ai = f.read()
    if "json.loads(content)" not in ai:
        errors.append("BUG: auto_ingestor.py _atomic_write does not validate JSON before writing")

# ----- 14. price_updater _atomic_write validates JSON -----
with open("src/automation/price_updater.py", encoding="utf-8") as f:
    pu = f.read()
    if "json.loads(content)" not in pu:
        errors.append("BUG: price_updater.py _atomic_write does not validate JSON")

# ----- 15. Check for any hardcoded llmcosts.pages.dev across ALL files -----
for root, dirs, files in os.walk("src"):
    for fname in files:
        if fname.endswith(".py"):
            fp = os.path.join(root, fname)
            with open(fp, encoding="utf-8") as f:
                content = f.read()
                if "llmcosts.pages.dev" in content:
                    errors.append(f"BUG: {fp} contains hardcoded llmcosts.pages.dev")

# Also check templates and dist config
for fp in ["build.py", "action.yml"]:
    with open(fp, encoding="utf-8") as f:
        if "llmcosts.pages.dev" in f.read():
            errors.append(f"BUG: {fp} contains hardcoded llmcosts.pages.dev")

# ----- RESULTS -----
print()
if errors:
    for e in errors:
        print(f"  [FAIL] {e}")
    print(f"\nTOTAL ERRORS: {len(errors)}")
else:
    print("  [PASS] ZERO ERRORS FOUND")
print()
