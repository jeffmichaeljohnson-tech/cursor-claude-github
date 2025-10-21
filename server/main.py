from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.responses import JSONResponse
import hmac, hashlib, os, json
from datetime import datetime

app = FastAPI(title="Claude Sync Bridge")

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

@app.post("/webhook/github")
async def handle_webhook(request: Request, x_hub_signature_256: str = Header(None), x_github_event: str = Header(None)):
    payload = await request.body()
    data = json.loads(payload)
    print(f"📥 {x_github_event}: {data.get('repository', {}).get('full_name')}")
    return JSONResponse(status_code=202, content={"status": "accepted"})

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}
