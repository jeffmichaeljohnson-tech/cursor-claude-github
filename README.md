# Always-Synced AI Dev Stack

Keeps Cursor, Claude, and GitHub synchronized so AI can reason over fresh context while GitHub remains the source of truth.

## Quick Start
1) Configure git hooks: `git config core.hooksPath hooks && chmod +x hooks/pre-commit`
2) Deploy FastAPI bridge from /server and set env vars
3) Add GitHub webhook (push) → bridge URL
4) Add Action secrets: CLAUDE_SYNC_URL, CLAUDE_SYNC_TOKEN
