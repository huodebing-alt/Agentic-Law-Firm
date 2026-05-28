#!/usr/bin/env python3
"""
sync-agents.py — mirrors .claude/agents/ to .agents/ for Antigravity.

Antigravity expects agents under `.agents/`; Claude Code expects them
under `.claude/agents/`. We keep the canonical files in `.claude/`
and mirror them here. Run any time you add or edit an agent.
"""
from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / ".claude" / "agents"
DST = ROOT / ".agents"


def main():
    if not SRC.exists():
        print(f"[sync-agents] source missing: {SRC}")
        return
    if DST.exists():
        # Wipe only generated mirror; keep .agents/README.md alone.
        # Permission errors on read-only mounts are tolerated — overwriting
        # in place still produces a consistent mirror.
        for child in DST.iterdir():
            if child.name == "README.md":
                continue
            try:
                if child.is_dir():
                    shutil.rmtree(child)
                else:
                    child.unlink()
            except (PermissionError, OSError):
                pass
    else:
        DST.mkdir(parents=True)
    n = 0
    for src_path in SRC.rglob("*"):
        if src_path.is_file():
            rel = src_path.relative_to(SRC)
            out = DST / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_path, out)
            n += 1
    print(f"[sync-agents] mirrored {n} files into {DST}")


if __name__ == "__main__":
    main()
