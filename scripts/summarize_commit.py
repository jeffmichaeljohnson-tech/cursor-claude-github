#!/usr/bin/env python3
import subprocess, sys

def run(*args):
    return subprocess.check_output(args).decode("utf-8", errors="ignore")

try:
    diff = run("git", "diff", "--cached", "--unified=0")
except Exception:
    sys.exit(0)

if not diff.strip():
    sys.exit(0)

files = run("git", "diff", "--cached", "--name-only").strip().splitlines()

print("\n### Summary")
print("- Files changed:")
for f in files:
    print(f"  - {f}")

print("\n### Notable TODOs / FIXMEs")
for f in files:
    try:
        content = run("git", "show", f":{f}")
    except Exception:
        continue
    hits = [ln for ln in content.splitlines() if "TODO" in ln or "FIXME" in ln]
    for h in hits[:10]:
        print(f"- {f}: {h.strip()[:200]}")
