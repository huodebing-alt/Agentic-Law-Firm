#!/usr/bin/env python3
"""
prepare-statutes.py — downloads / prepares the statute library for the
chosen jurisdictions.

CLI:
    --jurisdictions=cn,sg,us       (default: cn,sg,us)
    --selection=all|none|select:<keys>  (default: all)

Outputs to statutes/<jurisdiction>/<filename>.md.

Sources:
  * CN: zh.wikisource.org / npc.gov.cn (where available)
  * SG: sso.agc.gov.sg
  * US: law.cornell.edu

This script writes placeholder files with the source URL and a TODO
comment. Real scraping is left to the user under each source's
terms of use.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "statutes" / "manifest.json"

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


def write_placeholder(out_path: Path, name: str, url: str, jurisdiction: str):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    body = (
        f"# {name}\n\n"
        f"Jurisdiction: **{jurisdiction.upper()}**\n\n"
        f"Source URL: {url}\n\n"
        f"Status: placeholder. Real text not downloaded.\n\n"
        f"TODO: scrape from the source URL respecting their terms of use.\n"
    )
    out_path.write_text(body, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jurisdictions", default="cn,sg,us")
    ap.add_argument("--selection", default="all")
    args = ap.parse_args()

    jurisdictions = parse_list(args.jurisdictions, ALL_JURISDICTIONS)

    if not MANIFEST.exists():
        print(f"[prepare-statutes] missing manifest: {MANIFEST}")
        return
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    if isinstance(manifest, dict) and "statutes" in manifest and isinstance(manifest["statutes"], list):
        # legacy single-jurisdiction (CN) shape
        cn_list = manifest.get("statutes", [])
        manifest = {"cn": [{"name": x.get("title_cn", x.get("name", "")),
                            "url": x.get("url", ""),
                            "out": f"statutes/cn/{x.get('key', 'unknown')}.md"} for x in cn_list]}

    total = 0
    for j in jurisdictions:
        entries = manifest.get(j, [])
        all_keys = [e["name"] for e in entries]
        chosen = parse_selection(args.selection, all_keys)
        for e in entries:
            if e["name"] in chosen:
                out_path = ROOT / e["out"]
                write_placeholder(out_path, e["name"], e.get("url", ""), j)
                total += 1
        print(f"[prepare-statutes] {j}: prepared {len([e for e in entries if e['name'] in chosen])} files")
    print(f"[prepare-statutes] total {total} files written")


if __name__ == "__main__":
    main()
