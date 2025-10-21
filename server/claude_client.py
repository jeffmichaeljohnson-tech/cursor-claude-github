import os, requests

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20240620")
API_URL = "https://api.anthropic.com/v1/messages"

HEADERS = {
    "x-api-key": ANTHROPIC_API_KEY or "",
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
}

def summarize_commit(context: str) -> str:
    if not ANTHROPIC_API_KEY:
        return "No ANTHROPIC_API_KEY set; skipping summary."
    prompt = (
        "You are the project memory steward. Read the commit context and return: "
        "1) one-paragraph summary, 2) key risks, 3) next steps (bullets). Keep it under 180 words."
    )
    data = {
        "model": CLAUDE_MODEL,
        "max_tokens": 800,
        "messages": [
            {"role": "user", "content": f"{prompt}\n\n<commit>\n{context}\n</commit>"}
        ],
    }
    r = requests.post(API_URL, headers=HEADERS, json=data, timeout=30)
    r.raise_for_status()
    return r.json()["content"][0]["text"]
