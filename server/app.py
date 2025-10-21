from fastapi import FastAPI, Request, Header, HTTPException
from pydantic import BaseModel
import hmac, hashlib, os, subprocess, tempfile, requests
from .claude_client import summarize_commit

app = FastAPI()
GITHUB_WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET", "")
GH_TOKEN = os.getenv("GH_TOKEN")

class PushPayload(BaseModel):
    ref: str
    repository: dict
    head_commit: dict | None = None

def verify_signature(raw_body: bytes, signature: str | None):
    if not GITHUB_WEBHOOK_SECRET:
        return True
    if not signature:
        return False
    mac = hmac.new(GITHUB_WEBHOOK_SECRET.encode(), msg=raw_body, digestmod=hashlib.sha256)
    return hmac.compare_digest(f"sha256={mac.hexdigest()}", signature)

@app.post("/github/push")
async def on_push(request: Request, x_hub_signature_256: str | None = Header(None)):
    raw = await request.body()
    if not verify_signature(raw, x_hub_signature_256):
        raise HTTPException(401, "Invalid signature")

    payload = PushPayload.model_validate_json(raw)

    repo_url = payload.repository.get("clone_url")
    ref = payload.ref.split("/")[-1]

    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["git", "clone", "--depth", "20", repo_url, td], check=True)
        subprocess.run(["git", "checkout", ref], cwd=td, check=True)
        diff = subprocess.check_output(["git", "log", "-1", "-p", "--no-color"], cwd=td).decode("utf-8", errors="ignore")

    summary = summarize_commit(diff[:100_000])

    if GH_TOKEN and payload.head_commit:
        api = payload.repository.get("url")
        sha = payload.head_commit.get("id")
        requests.post(
            f"{api}/commits/{sha}/comments",
            headers={"Authorization": f"Bearer {GH_TOKEN}", "Accept": "application/vnd.github+json"},
            json={"body": f"### Claude Summary\n\n{summary}"},
            timeout=20,
        )

    return {"ok": True, "summary_preview": summary[:200]}
