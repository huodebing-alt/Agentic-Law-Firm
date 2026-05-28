#!/usr/bin/env python3
"""
onboard.py — runs the configuration step of /onboard.

Invoked by the onboarding-host agent via the Bash tool. Reads CLI
args, writes .agentic-law-firm-config.json, optionally calls
install-mcp.py and prepare-statutes.py.
"""
from __future__ import annotations
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / ".agentic-law-firm-config.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--area", choices=["corporate", "individual", "both"], default="both")
    ap.add_argument("--mcp", default="all", help="all / select:name1,name2 / none")
    ap.add_argument("--statutes", default="all", help="all / select:name1,name2 / none")
    ap.add_argument("--hard-gates", choices=["on", "off"], default="on")
    ap.add_argument("--threshold", type=int, default=100_000_000, help="hard-gate deal-value threshold in CNY")
    ap.add_argument("--role", choices=["solo", "firm", "in-house", "learning"], default="solo")
    ap.add_argument("--language", default="zh-CN")
    args = ap.parse_args()

    config = {
        "practice_area": args.area,
        "mcp_install": args.mcp,
        "statutes": args.statutes,
        "hard_gates": {
            "enabled": args.hard_gates == "on",
            "deal_value_threshold": args.threshold,
            "currency": "CNY",
        },
        "identity": args.role,
        "language": args.language,
        "matters": [],
    }
    CONFIG_PATH.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[onboard] wrote {CONFIG_PATH}")

    # Hand off to install-mcp and prepare-statutes for the actual work
    env = os.environ.copy()
    if args.mcp != "none":
        subprocess.run([sys.executable, str(ROOT / "scripts" / "install-mcp.py"),
                        "--selection", args.mcp], check=False, env=env)
    if args.statutes != "none":
        subprocess.run([sys.executable, str(ROOT / "scripts" / "prepare-statutes.py"),
                        "--selection", args.statutes], check=False, env=env)

    print("[onboard] done. Type /onboard again any time to reconfigure.")
    print("[onboard] suggested first skill: contract-review-cn (审一份中文合同)")


if __name__ == "__main__":
    main()
