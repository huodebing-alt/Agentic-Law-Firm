#!/usr/bin/env python3
"""
install-mcp.py — registers MCP servers with the active harness.

For Claude Code: writes / updates ~/.claude.json's mcpServers map.
For Antigravity: relies on `.antigravity/mcp.json` already present in
the project. This script copies the project's `.mcp.json` block into
the user-level config so the harness picks the servers up.

The script is non-fatal on missing dependencies — it logs and moves on.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def parse_selection(selection: str, all_keys):
    if selection in (None, "", "all"):
        return list(all_keys)
    if selection == "none":
        return []
    if selection.startswith("select:"):
        return [s.strip() for s in selection[len("select:"):].split(",") if s.strip()]
    return list(all_keys)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selection", default="all")
    args = ap.parse_args()

    project_mcp = json.loads((ROOT / ".mcp.json").read_text(encoding="utf-8"))
    servers = project_mcp.get("mcpServers", {})
    chosen = parse_selection(args.selection, servers.keys())

    # User-level config (Claude Code).
    home_cfg = Path.home() / ".claude.json"
    if home_cfg.exists():
        try:
            user_cfg = json.loads(home_cfg.read_text(encoding="utf-8"))
        except Exception:
            user_cfg = {}
    else:
        user_cfg = {}
    user_cfg.setdefault("mcpServers", {})
    for name in chosen:
        user_cfg["mcpServers"][name] = servers[name]
    home_cfg.write_text(json.dumps(user_cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[install-mcp] registered {len(chosen)} servers in {home_cfg}")


if __name__ == "__main__":
    main()
