# Project Memory

## Purpose
Single source of truth for context Claude and developers should retain across sessions.

## Current Direction
- Architecture: Cursor for local context + GitHub as canonical + Claude for reasoning
- Branching: trunk-based (main) with short-lived feature branches

## Key Decisions (reverse-chron)
- <YYYY-MM-DD>: Initial template enabled; commit summaries auto-sent to Claude; PR summaries posted by workflow

## Open Questions
- [ ] Which directories should be excluded from AI context? (see rules.md)
- [ ] Red-teaming checklist for AI output on PRs

## Commit 2025-10-20T22:42:34-0400

### Summary
- Files changed:
  - .context/memory.md
  - .context/rules.md
  - .env.example
  - .github/workflows/summarize-commits.yml
  - .gitignore
  - README.md
  - SECURITY.md
  - hooks/pre-commit
  - scripts/post_to_claude.py
  - scripts/summarize_commit.py
  - server/app.py
  - server/claude_client.py
  - server/requirements.txt

### Notable TODOs / FIXMEs
- scripts/summarize_commit.py: print("\n### Notable TODOs / FIXMEs")
- scripts/summarize_commit.py: hits = [ln for ln in content.splitlines() if "TODO" in ln or "FIXME" in ln]

## Commit 2025-10-20T22:43:45-0400

### Summary
- Files changed:
  - SYNC.md

### Notable TODOs / FIXMEs
