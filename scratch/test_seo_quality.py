import os
import json
import sys
from pathlib import Path

# Add repo root to path
sys.path.insert(0, str(Path(os.getcwd())))

from src.core.groq_client import get_groq_client

def test_quality():
    with open('data/models.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        models = data['models']
    
    # Selecting two high-intent models
    m1 = next(m for m in models if '405b' in m['id'].lower())
    m2 = next(m for m in models if 'gpt-4o' in m['id'].lower() and 'mini' not in m['id'].lower())
    
    name_a = m1.get('name', m1['id'])
    name_b = m2.get('name', m2['id'])
    
    client = get_groq_client()
    if not client:
        print("Error: No Groq Client")
        return

    prompt = f"""
    You are a Staff Software Engineer and CTO. Write a highly technical, objective, formatting-heavy 
    comparative analysis comparing two LLMs for a technical audience on Dev.to: {name_a} vs {name_b}.
    
    IMPORTANT SEO RULES:
    1. Use a click-worthy but professional H1 title.
    2. Use H2 and H3 headers for clear hierarchy.
    3. Include tables comparing Token/Sec, Cost/1M Tokens, and Context Window.
    4. Write a section on 'Production Readiness' and 'When to Choose Which'.
    5. Include a sample JSON configuration for routing between these two in LiteLLM.
    
    Structure the article:
    1. Executive Summary
    2. Architecture & Tech Specs
    3. Context Window & Token Limits
    4. Pricing Breakdown (compare their API costs)
    5. Production Routing & Deployment Strategy
    
    Keep the tone extremely professional. Use markdown, bold headers, and bullet points.
    Do NOT sound like a marketer. Sound like an engineer posting on Dev.to.
    """

    print(f"Generating sample article: {name_a} vs {name_b}...")
    content = client.generate(
        system_prompt="You are a Staff Software Engineer and CTO at a major tech firm.",
        user_prompt=prompt
    )
    
    output_path = Path("artifacts/sample_article_preview.md")
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("SUCCESS: Sample article saved to artifacts/sample_article_preview.md")

if __name__ == "__main__":
    test_quality()
