import os
import sys
import json
import requests
from pathlib import Path
from datetime import datetime

# Add GitHub Automation project root to path for unified services if present
GITHUB_AUTO_PATH = Path(__file__).resolve().parent.parent / "GITHUB Automation"
if GITHUB_AUTO_PATH.exists() and str(GITHUB_AUTO_PATH) not in sys.path:
    sys.path.insert(0, str(GITHUB_AUTO_PATH))

try:
    from backend.config import get_config
    cfg = get_config()
    OLLAMA_HOST = cfg.get("OLLAMA_HOST", "http://localhost:11434")
    OLLAMA_MODEL = cfg.get("OLLAMA_MODEL", "qwen3:4b")
    GEMINI_API_KEY = cfg.get("GEMINI_API_KEY", "")
    LINKEDIN_ACCESS_TOKEN = cfg.get("LINKEDIN_ACCESS_TOKEN", "")
    PERSON_ID = cfg.get("LINKEDIN_PERSON_ID", "")
except Exception:
    OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
    OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "qwen3:4b")
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
    LINKEDIN_ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN", "")
    PERSON_ID = os.environ.get("LINKEDIN_PERSON_ID", "")

# Ollama API URL
OLLAMA_URL = f"{OLLAMA_HOST.rstrip('/')}/api/generate"

# Gemini API URL
GEMINI_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/"
    f"gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
)

# LinkedIn REST API
LINKEDIN_URL = "https://api.linkedin.com/rest/posts"

def _clean_json_text(raw_text: str) -> dict:
    """Safely extract and parse JSON from LLM output, removing think tags and code blocks."""
    import re
    # Strip <think>...</think> tags if model outputted reasoning
    cleaned = re.sub(r"<think>[\s\S]*?</think>", "", raw_text).strip()
    
    # Strip markdown code blocks
    if "```json" in cleaned:
        cleaned = cleaned.split("```json")[1].split("```")[0].strip()
    elif "```" in cleaned:
        cleaned = cleaned.split("```")[1].split("```")[0].strip()
        
    try:
        return json.loads(cleaned)
    except Exception:
        # Regex search for the first JSON object
        m = re.search(r'(\{[\s\S]*\})', cleaned)
        if m:
            return json.loads(m.group(1))
        raise ValueError(f"Could not parse JSON from model output: {raw_text[:200]}")

# Ensure UTF-8 output encoding on Windows console
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Ensure UTF-8 output encoding on Windows console
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ==========================================
# STEP 1 : Generate Post
# ==========================================
def generate_post(topic="AI and Software Engineering"):
    prompt = f"""Generate a professional LinkedIn post about {topic}.
Topic should be related to AI, Programming, Career Growth, Technology.

Rules:
- 120-180 words
- Add emojis
- Add 5 hashtags
- Return ONLY JSON

Example:
{{
 "topic": "AI",
 "post_text": "Exciting advancements in AI..."
}}
"""

    # 1. Try Local Ollama (qwen3:4b) first
    try:
        print(f"[Ollama] Calling local Ollama [{OLLAMA_MODEL}] at {OLLAMA_HOST}...")
        chat_url = f"{OLLAMA_HOST.rstrip('/')}/v1/chat/completions"
        chat_payload = {
            "model": OLLAMA_MODEL,
            "messages": [
                {"role": "system", "content": "You are a professional LinkedIn post generator. Return ONLY valid JSON."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "response_format": {"type": "json_object"}
        }
        res = requests.post(chat_url, json=chat_payload, timeout=180)
        if res.status_code == 200:
            raw_text = res.json()["choices"][0]["message"]["content"].strip()
            data = _clean_json_text(raw_text)
            print(f"[Ollama] Generated successfully with [{OLLAMA_MODEL}]")
            return data
    except Exception as e:
        print(f"[Ollama] Chat API failed: {e}. Trying /api/generate fallback...")
        try:
            ollama_payload = {
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.7}
            }
            res = requests.post(OLLAMA_URL, json=ollama_payload, timeout=180)
            if res.status_code == 200:
                raw_text = res.json().get("response", "")
                data = _clean_json_text(raw_text)
                print(f"[Ollama] Generated successfully with [{OLLAMA_MODEL}]")
                return data
        except Exception as e2:
            print(f"[Ollama] Fallback also failed: {e2}. Trying Gemini...")

    # 2. Fallback to Gemini if API key is provided
    if GEMINI_API_KEY and GEMINI_API_KEY != "assd":
        print("Calling Google Gemini API...")
        gemini_payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ],
            "generationConfig": {
                "temperature": 0.8,
                "responseMimeType": "application/json"
            }
        }
        response = requests.post(GEMINI_URL, json=gemini_payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        raw_json = data["candidates"][0]["content"]["parts"][0]["text"]
        return _clean_json_text(raw_json)

    raise RuntimeError("No AI provider succeeded. Make sure Ollama is running (`ollama run qwen3:4b`) or valid GEMINI_API_KEY is configured.")

# ==========================================
# STEP 2 : Publish to LinkedIn
# ==========================================
def publish_post(post_text):
    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "LinkedIn-Version": "202604",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }

    body = {
        "author": f"urn:li:person:{PERSON_ID}",
        "commentary": post_text,
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": []
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False
    }

    response = requests.post(
        LINKEDIN_URL,
        headers=headers,
        json=body,
        timeout=60
    )
    response.raise_for_status()
    return response.status_code

# ==========================================
# STEP 3 : Save Log
# ==========================================
def save_log(topic, status):
    log_file = Path(__file__).resolve().parent / "post_log.txt"
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()} | {topic} | {status}\n")

# ==========================================
# MAIN
# ==========================================
def main():
    print("Generating post with Gemini...")
    post = generate_post()
    print("\nTopic:", post.get("topic"))
    print("\n" + post.get("post_text", "") + "\n")

    print("Posting to LinkedIn...")
    status = publish_post(post["post_text"])
    save_log(post["topic"], status)
    print("Successfully Posted.")
    print("HTTP Status:", status)

if __name__ == "__main__":
    main()