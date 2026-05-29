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


def check_environment() -> None:
    """Abort if Python < 3.10 or pip is unavailable."""
    if sys.version_info < (3, 10):
        print(f"[onboard] ERROR: Python {sys.version.split()[0]} found, but Agentic-Law-Firm "
              f"requires >= 3.10. See README section 2 (Prerequisites).", file=sys.stderr)
        sys.exit(2)
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"],
                       check=True, capture_output=True)
    except Exception as exc:
        print(f"[onboard] ERROR: pip not available: {exc}. See README section 2.", file=sys.stderr)
        sys.exit(2)


def install_mcp_deps() -> None:
    """Run scripts/install-mcp-deps.sh so every local MCP server can launch."""
    script = ROOT / "scripts" / "install-mcp-deps.sh"
    if not script.exists():
        print(f"[onboard] WARN: {script} not found; skipping MCP-deps install.")
        return
    print(f"[onboard] running: bash {script}")
    rc = subprocess.run(["bash", str(script)], check=False).returncode
    if rc != 0:
        print(f"[onboard] WARN: install-mcp-deps.sh exited with code {rc}. "
              f"Some MCP servers may fail to launch.", file=sys.stderr)


def test_mcp_servers() -> int:
    """Smoke-test every MCP server; return the number of failures."""
    script = ROOT / "scripts" / "test-mcp.sh"
    if not script.exists():
        print(f"[onboard] WARN: {script} not found; skipping MCP self-test.")
        return 0
    print(f"[onboard] running: bash {script}")
    rc = subprocess.run(["bash", str(script)], check=False).returncode
    return rc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jurisdictions", default="cn,sg,us")
    ap.add_argument("--mcps", default="all")
    ap.add_argument("--statutes", default="all")
    ap.add_argument("--hard-gates", default="yes")
    ap.add_argument("--identity", default="solo")
    ap.add_argument("--threshold", type=int, default=1_000_000)
    ap.add_argument("--skip-env-check", action="store_true",
                    help="skip Python + pip preflight (not recommended)")
    ap.add_argument("--skip-install", action="store_true",
                    help="skip install-mcp-deps.sh (assume venv already set up)")
    ap.add_argument("--skip-selftest", action="store_true",
                    help="skip test-mcp.sh at the end")
    args = ap.parse_args()

    # Step 0 — environment
    if not args.skip_env_check:
        check_environment()

    # Step 1 — MCP deps (this is what the wizard previously forgot)
    if not args.skip_install:
        install_mcp_deps()

    # Step 2 — collected answers (already in args)
    jurisdictions = parse_list(args.jurisdictions, ALL_JURISDICTIONS)
    invalid = [j for j in jurisdictions if j not in ALL_JURISDICTIONS]
    if invalid:
        print(f"[onboard] unknown jurisdictions: {invalid}", file=sys.stderr)
        sys.exit(2)

    print(f"[onboard] jurisdictions: {jurisdictions}")
    print(f"[onboard] identity: {args.identity}")
    print(f"[onboard] hard-gates: {args.hard_gates} (threshold {args.threshold})")

    # Step 3a — Install/register MCPs
    mcp_args = ["python3", str(ROOT / "scripts" / "install-mcp.py"),
                "--jurisdictions", ",".join(jurisdictions),
                "--selection", args.mcps]
    print(f"[onboard] running: {' '.join(mcp_args)}")
    subprocess.run(mcp_args, check=False)

    # Step 3b — Prepare statute library
    statutes_args = ["python3", str(ROOT / "scripts" / "prepare-statutes.py"),
                     "--jurisdictions", ",".join(jurisdictions),
                     "--selection", args.statutes]
    print(f"[onboard] running: {' '.join(statutes_args)}")
    subprocess.run(statutes_args, check=False)

    # Step 3c — Persist config
    config = {
        "version": "0.3",
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

    # Step 4 — MCP smoke test
    if not args.skip_selftest:
        rc = test_mcp_servers()
        if rc != 0:
            print(f"[onboard] WARN: test-mcp.sh reported failures. "
                  f"Re-run 'bash scripts/install-mcp-deps.sh' or inspect the "
                  f"failing server's README.", file=sys.stderr)

    print("[onboard] done")


if __name__ == "__main__":
    main()
