"""
GOD-LEVEL PARASITE SYNDICATION ENGINE
Generates highly technical VS Showdown articles via Groq Llama-3
and automatically publishes them to Dev.to (DR 93) to bypass Google Sandbox.
"""
import os
import json
import random
import logging
import sys
import requests
from typing import Optional

# Setup Pathing (running from repo root)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__name__), "..", "..")))

from src.core.groq_client import get_groq_client

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

MODELS_JSON = "data/models.json"
DEVTO_API_URL = "https://dev.to/api/articles"
AFFILIATE_URL = "https://m.do.co/c/your_digitalocean_affiliate_id_here" # Placeholder until user sets it up
AFFILIATE_LINK_TEXT = "For deploying these models in production, we strictly recommend spinning up an isolated Vultr or DigitalOcean droplet to minimize latency. [Get $200 free credit here](" + AFFILIATE_URL + ")."


def load_models() -> list[dict]:
    try:
        with open(MODELS_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Filter for models that have proper IDs and pricing
            valid_models = []
            for m in data:
                if m.get('id') and m.get('pricing'):
                    valid_models.append(m)
            return valid_models
    except Exception as e:
        logger.error(f"Failed to load models: {e}")
        return []

def generate_devto_article(model_a: dict, model_b: dict) -> Optional[dict]:
    """Uses Groq to generate a 1,500 word CTO-level VS showdown."""
    client = get_groq_client()
    if not client:
        return None

    name_a = model_a.get('name', model_a['id'])
    name_b = model_b.get('name', model_b['id'])
    
    # Prompt explicitly designed to mimic a professional, CTO-level engineer
    prompt = f"""
    You are a Staff Software Engineer and CTO. Write a highly technical, objective, formatting-heavy 
    comparative analysis comparing two LLMs: {name_a} vs {name_b}.
    
    Structure the article:
    1. Executive Summary
    2. Architecture & Tech Specs
    3. Context Window & Token Limits
    4. Pricing Breakdown (compare their API costs)
    5. Production Routing & Deployment Strategy
    
    Keep the tone extremely professional. Use markdown, bold headers, and bullet points.
    Do NOT sound like a marketer. Sound like an engineer posting on Dev.to.
    """

    logger.info(f"Generating VS Showdown for {name_a} vs {name_b}...")
    
    # Call Groq (assuming the wrapper returns a string response directly or parses it)
    # The client.generate returns a string (the text content of the response) for standard usage in LLMCosts.
    try:
        content = client.generate(
            prompt=prompt,
            model="llama-3.3-70b-versatile"
        )
        if not content:
            return None
        
        # Append Affiliate Trap
        final_content = f"{content}\n\n---\n\n### Production Deployment Tips\n{AFFILIATE_LINK_TEXT}"
        title = f"LLM Cost Showdown: {name_a} vs {name_b} in Production"
        
        return {
            "title": title,
            "body": final_content
        }
    except Exception as e:
        logger.error(f"Groq API failure during article generation: {e}")
        return None


def publish_to_devto(article_dict: dict, devto_key: str):
    """Pushes the article to Dev.to using their public API."""
    headers = {
        "api-key": devto_key,
        "Content-Type": "application/json"
    }
    
    payload = {
        "article": {
            "title": article_dict["title"],
            "body_markdown": article_dict["body"],
            "published": True,
            "tags": ["ai", "llm", "machinelearning", "programming"],
            "canonical_url": f"https://llmcosts.dev/compare/{article_dict['title'].lower().replace(' ', '-')}"
        }
    }

    logger.info(f"Publishing to Dev.to: {article_dict['title']}")
    
    try:
        response = requests.post(DEVTO_API_URL, headers=headers, json=payload, timeout=30)
        if response.status_code == 201:
            logger.info("✅ Successfully published to Dev.to!")
            logger.info(f"URL: {response.json().get('url')}")
        else:
            logger.error(f"Failed to publish. Status: {response.status_code}. Response: {response.text}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error while reaching Dev.to: {e}")

def run_pipeline():
    # 1. Null-Safe Key Check
    # We exit gracefully (code 0) so we never crash the GitHub Action if the secret is missing.
    devto_key = os.getenv("DEVTO_API_KEY")
    if not devto_key:
        logger.warning("DEVTO_API_KEY is not set in environment. Skipping Parasite Syndication pipeline to avoid breaking build.")
        sys.exit(0)
        
    models = load_models()
    if len(models) < 2:
        logger.warning("Not enough models loaded to run VS pipeline.")
        sys.exit(0)
        
    # Pick two random valid models
    m1, m2 = random.sample(models, 2)
    
    article_data = generate_devto_article(m1, m2)
    if article_data:
        publish_to_devto(article_data, devto_key)
    else:
        logger.error("Failed to generate article payload.")


if __name__ == "__main__":
    logger.info("Initializing Dev.to Parasite Pipeline...")
    run_pipeline()
    logger.info("Pipeline Execution Complete.")
