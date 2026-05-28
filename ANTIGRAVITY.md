# Agentic-Law-Firm (Google Antigravity entry)

This file is loaded by Google Antigravity (`agy`) when you open the
project. It is intentionally short — all operating rules live in
`AGENTS.md` at the project root.

Antigravity-specific layout in this repo:
- `.agents/` mirrors `.claude/agents/` (kept in sync by
  `scripts/sync-agents.py`)
- `.antigravity/mcp.json` mirrors `.mcp.json`
- Skills live in `.claude/skills/` (Antigravity reads them via the
  standard SKILL.md format; no duplication needed)

Useful CLI:
- `agy inspect` — show all loaded agents, skills, MCPs
- `agy run <agent>` — invoke an agent manually
- `agy mcp test <name>` — round-trip a tool call on an MCP

First-time setup: launch Antigravity in this directory, then type
`/onboard` in the chat.
