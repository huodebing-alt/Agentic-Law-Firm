#!/usr/bin/env python3
"""
prepare-statutes.py — downloads selected statutes per manifest.

For v0.1 this is a stub: it only writes empty placeholder files at
statutes/data/<key>.md so downstream agents can find them. Real
downloads are wired in a follow-up version.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "statutes" / "data"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selection", default="all")
    args = ap.parse_args()

    manifest = json.loads((ROOT / "statutes" / "manifest.json").read_text(encoding="utf-8"))
    statutes = manifest["statutes"]

    if args.selection == "none":
        print("[prepare-statutes] selection=none. Skipping.")
        return

    if args.selection.startswith("select:"):
        keys = [s.strip() for s in args.selection[len("select:"):].split(",") if s.strip()]
        statutes = [s for s in statutes if s["key"] in keys]

    DATA.mkdir(parents=True, exist_ok=True)
    for s in statutes:
        path = DATA / f"{s['key']}.md"
        placeholder = (
            f"# {s['title_cn']} ({s['title_en']})\n\n"
            f"- Key: {s['key']}\n"
            f"- Effective: {s.get('effective', 'unknown')}\n"
            f"- Source: {s.get('source', 'flk.npc.gov.cn')}\n\n"
            f"## Status\n\n"
            f"Placeholder. Real text will be downloaded by a future version of this script.\n"
        )
        path.write_text(placeholder, encoding="utf-8")
        print(f"[prepare-statutes] {path.name}")
    print(f"[prepare-statutes] prepared {len(statutes)} statute placeholders.")


if __name__ == "__main__":
    main()
