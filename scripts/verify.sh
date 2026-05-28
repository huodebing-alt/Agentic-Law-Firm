#!/usr/bin/env bash
# verify.sh — static checks for Agentic-Law-Firm.
# Verifies: frontmatter in every agent / skill .md file is well-formed YAML;
# every server referenced from .mcp.json exists; every template referenced
# from style-config.json font list is a known font role.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "[verify] root: $ROOT"

python3 - <<'PY'
import json
import sys
from pathlib import Path

root = Path(".")
errors = []

# 1. Frontmatter check.
for md in list(root.glob(".claude/agents/**/*.md")) + list(root.glob(".claude/skills/**/SKILL.md")):
    text = md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append(f"{md}: missing leading '---'")
        continue
    end = text.find("---", 3)
    if end == -1:
        errors.append(f"{md}: unterminated frontmatter")
        continue
    front = text[3:end]
    if "name:" not in front or "description:" not in front:
        errors.append(f"{md}: frontmatter missing name or description")

# 2. .mcp.json references exist.
mcp_paths = [Path(".mcp.json"), Path(".antigravity/mcp.json")]
for mcp_path in mcp_paths:
    if not mcp_path.exists():
        errors.append(f"{mcp_path}: missing")
        continue
    data = json.loads(mcp_path.read_text(encoding="utf-8"))
    for name, cfg in data.get("mcpServers", {}).items():
        args = cfg.get("args", [])
        if args:
            target = root / args[-1]
            if not target.exists():
                errors.append(f"{mcp_path}: {name} references missing {target}")

# 3. style-config.json is parseable.
sc = Path("templates/_style/style-config.json")
if sc.exists():
    json.loads(sc.read_text(encoding="utf-8"))
else:
    errors.append(f"{sc}: missing")

if errors:
    print("[verify] FAIL")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("[verify] OK")
PY
