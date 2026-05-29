#!/usr/bin/env python3
"""
onboard.py — wires up the user's chosen jurisdictions, MCPs, statutes,
hard-gates, and identity.

CLI:
    --jurisdictions=cn,sg,us       (default: cn,sg,us)
    --mcps=all|none|select:<keys>  (default: all-for-chosen-jurisdictions)
    --statutes=all|none|select:<keys>  (default: all-for-chosen-jurisdictions)
    --hard-gates=yes|no            (default: yes)
    --identity=solo|firm|in-house|learning  (default: solo)
    --threshold=<int RMB / SGD / USD>   (default: 1000000)
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ALL_JURISDICTIONS = ["cn", "sg", "us"]


def parse_list(s: str, fallback: list[str]) -> list[str]:
    if s in (None, "", "all"):
        return list(fallback)
    if s == "none":
        return []
    return [x.strip() for x in s.split(",") if x.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jurisdictions", default="cn,sg,us")
    ap.add_argument("--mcps", default="all")
    ap.add_argument("--statutes", default="all")
    ap.add_argument("--hard-gates", default="yes")
    ap.add_argument("--identity", default="solo")
    ap.add_argument("--threshold", type=int, default=1_000_000)
    args = ap.parse_args()

    jurisdictions = parse_list(args.jurisdictions, ALL_JURISDICTIONS)
    invalid = [j for j in jurisdictions if j not in ALL_JURISDICTIONS]
    if invalid:
        print(f"[onboard] unknown jurisdictions: {invalid}", file=sys.stderr)
        sys.exit(2)

    print(f"[onboard] jurisdictions: {jurisdictions}")
    print(f"[onboard] identity: {args.identity}")
    print(f"[onboard] hard-gates: {args.hard_gates} (threshold {args.threshold})")

    # 1. Install MCPs
    mcp_args = ["python3", str(ROOT / "scripts" / "install-mcp.py"),
                "--jurisdictions", ",".join(jurisdictions),
                "--selection", args.mcps]
    print(f"[onboard] running: {' '.join(mcp_args)}")
    subprocess.run(mcp_args, check=False)

    # 2. Prepare statute library
    statutes_args = ["python3", str(ROOT / "scripts" / "prepare-statutes.py"),
                     "--jurisdictions", ",".join(jurisdictions),
                     "--selection", args.statutes]
    print(f"[onboard] running: {' '.join(statutes_args)}")
    subprocess.run(statutes_args, check=False)

    # 3. Write config
    config = {
        "version": "0.2",
        "jurisdictions": jurisdictions,
        "mcps": args.mcps,
        "statutes": args.statutes,
        "hard_gates": args.hard_gates == "yes",
        "deal_threshold": args.threshold,
        "identity": args.identity,
    }
    config_path = ROOT / ".agentic-law-firm-config.json"
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[onboard] wrote config: {config_path}")

    print("[onboard] done")


if __name__ == "__main__":
    main()
