#!/usr/bin/env python3
import os, sys, json, requests

CLAUDE_SYNC_URL = os.getenv("CLAUDE_SYNC_URL")
CLAUDE_SYNC_TOKEN = os.getenv("CLAUDE_SYNC_TOKEN")

payload = json.loads(sys.stdin.read()) if not sys.stdin.isatty() else {}

headers = {
    "Authorization": f"Bearer {CLAUDE_SYNC_TOKEN}" if CLAUDE_SYNC_TOKEN else "",
    "Content-Type": "application/json",
}

r = requests.post(CLAUDE_SYNC_URL, headers=headers, data=json.dumps(payload), timeout=20)
print(r.status_code)
print(r.text)
