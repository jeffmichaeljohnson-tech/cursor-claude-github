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
