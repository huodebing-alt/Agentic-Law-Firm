# `.agents/` — Antigravity mirror

This directory holds an exact mirror of `.claude/agents/` for the
benefit of Google Antigravity, which reads agents from `.agents/`
by convention.

Do not edit files here directly. The canonical source is
`.claude/agents/`. Run `python3 scripts/sync-agents.py` to
regenerate this mirror after any agent edit.
