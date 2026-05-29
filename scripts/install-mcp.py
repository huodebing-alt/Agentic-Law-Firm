#!/usr/bin/env python3
"""
install-mcp.py — registers MCP servers with the active harness.

For Claude Code: writes / updates ~/.claude.json's mcpServers map.
For Antigravity: relies on `.antigravity/mcp.json` already present in
the project.

CLI:
    --jurisdictions=cn,sg,us       (default: cn,sg,us)
    --selection=all|none|select:<keys>  (default: all)

Jurisdiction filter: filters the project's `.mcp.json` to keys that match
the jurisdiction prefix conventions:
  * cn → keys without 'sg-' or 'us-' prefix (legacy flat layout)
  * sg → keys starting with 'sg-'
  * us → keys starting with 'us-'

The script is non-fatal on missing dependencies — it logs and moves on.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ALL_JURISDICTIONS = ["cn", "sg", "us"]


def parse_list(s: str, fallback: list[str]) -> list[str]:
    if s in (None, "", "all"):
        return list(fallback)
    if s == "none":
        return []
    return [x.strip() for x in s.split(",") if x.strip()]


def parse_selection(selection: str, all_keys):
    if selection in (None, "", "all"):
        return list(all_keys)
    if selection == "none":
        return []
    if selection.startswith("select:"):
        return [s.strip() for s in selection[len("select:"):].split(",") if s.strip()]
    return list(all_keys)


def filter_by_jurisdiction(keys: list[str], jurisdictions: list[str]) -> list[str]:
    out = []
    for k in keys:
        if k.startswith("sg-"):
            if "sg" in jurisdictions:
                out.append(k)
        elif k.startswith("us-"):
            if "us" in jurisdictions:
                out.append(k)
        else:
            # legacy flat-layout = CN
            if "cn" in jurisdictions:
                out.append(k)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jurisdictions", default="cn,sg,us")
    ap.add_argument("--selection", default="all")
    args = ap.parse_args()

    jurisdictions = parse_list(args.jurisdictions, ALL_JURISDICTIONS)

    project_mcp = json.loads((ROOT / ".mcp.json").read_text(encoding="utf-8"))
    servers = project_mcp.get("mcpServers", {})
    all_keys = list(servers.keys())
    jurisdictional = filter_by_jurisdiction(all_keys, jurisdictions)
    chosen = parse_selection(args.selection, jurisdictional)
    # also restrict to jurisdictional set
    chosen = [k for k in chosen if k in jurisdictional]

    print(f"[install-mcp] jurisdictions: {jurisdictions}")
    print(f"[install-mcp] {len(chosen)} of {len(all_keys)} MCPs selected")
    for k in chosen:
        print(f"  - {k}")

    # User-level config (Claude Code).
    user_cfg_path = Path.home() / ".claude.json"
    if user_cfg_path.exists():
        try:
            user_cfg = json.loads(user_cfg_path.read_text(encoding="utf-8"))
        except Exception:
            user_cfg = {}
    else:
        user_cfg = {}
    user_cfg.setdefault("mcpServers", {})
    for k in chosen:
        user_cfg["mcpServers"][k] = servers[k]
    try:
        user_cfg_path.parent.mkdir(parents=True, exist_ok=True)
        user_cfg_path.write_text(json.dumps(user_cfg, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[install-mcp] updated {user_cfg_path}")
    except OSError as e:
        print(f"[install-mcp] note: could not write {user_cfg_path}: {e}")

    print("[install-mcp] done")


if __name__ == "__main__":
    main()
