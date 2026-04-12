import json
from pathlib import Path

DB_PATH = Path(r"C:\Users\adars\Downloads\manju\data\models.json")

def purge_hallucinations():
    try:
        data = json.loads(DB_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error loading models.json: {e}")
        return

    original_count = len(data.get("models", []))
    clean_models = []
    
    hallucination_keywords = ["gemma 4", "llama 4", "llama-4"]

    for m in data.get("models", []):
        name = m.get("name", "").lower()
        slug = m.get("slug", "").lower()
        model_id = m.get("id", "").lower()

        # Check for bad keywords
        is_fake = any(hw in name or hw in slug or hw in model_id for hw in hallucination_keywords)
        
        # Check for fake future dates (e.g., year 2026 for unreleased stuff)
        # Wait, some legitimate models might technically have a release_date=2026 since we're in 2026.
        # So we'll skip date checks and trust the keywords.
        
        # Check pricing anomaly (negative pricing)
        pricing = m.get("pricing") or {}
        has_negative_price = any(v < 0 for v in pricing.values() if isinstance(v, (int, float)))

        if is_fake or has_negative_price:
            print(f"Purging hallucinated/corrupted model: {m.get('id')}")
            continue
            
        clean_models.append(m)

    data["models"] = clean_models
    new_count = len(clean_models)
    
    DB_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Purge complete! Removed {original_count - new_count} corrupted entries.")

if __name__ == "__main__":
    purge_hallucinations()
