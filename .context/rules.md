# AI Context Rules

## Include
- /src, /server, README, ADRs, docs, workflows

## Exclude
- Secrets, .env, node_modules, build artifacts, large binaries, personal data

## Redaction
- If a diff contains credentials or keys, redact before sending to Claude.
