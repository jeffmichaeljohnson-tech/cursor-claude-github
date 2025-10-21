# Security Guidance

- Require HTTPS and a long bearer token (for Action→bridge if enabled)
- Use GitHub webhook HMAC (x-hub-signature-256) and verify on server
- Use read-only GH tokens for posting comments
- Never send .env or secrets to Claude; keep a denylist in .context/rules.md
- Log minimal metadata; avoid storing raw diffs server-side
