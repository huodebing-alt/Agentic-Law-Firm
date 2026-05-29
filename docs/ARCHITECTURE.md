# Architecture

## Overview

Agentic-Law-Firm is a layered file-only system. There is no service,
no daemon, no database — just markdown / json / python files that a
model-agnostic agent harness (Claude Code, Google Antigravity) loads
when the user opens the project directory.

## Layers

```
+---------------------------------------------------------------+
| Layer 5 — Operator                                            |
|   The lawyer typing into Antigravity / Claude Code            |
+---------------------------------------------------------------+
| Layer 4 — Slash commands                                      |
|   .claude/commands/*.md   (e.g. /onboard)                     |
+---------------------------------------------------------------+
| Layer 3 — Agents                                              |
|   .claude/agents/<group>/*.md                                 |
|   (task-router, specialists, doc-ops, research, drafting)     |
+---------------------------------------------------------------+
| Layer 2 — Skills                                              |
|   .claude/skills/<group>/<skill>/SKILL.md                     |
|   (workflow recipes the agents can dispatch)                  |
+---------------------------------------------------------------+
| Layer 1 — MCP connectors                                      |
|   mcp-servers/<name>/server.py                                |
|   (statutes-rag, wenshu, samr, cnipa, tianyancha, ...)        |
+---------------------------------------------------------------+
| Layer 0 — Static assets                                       |
|   templates/ (docx)                                           |
|   statutes/ (downloaded laws)                                 |
|   .agentic-law-firm-config.json                               |
+---------------------------------------------------------------+
```

The orchestrator agents (task-router, task-decomposer, aggregator,
hard-gate-keeper) live at Layer 3 alongside the specialists; their
role is to control the call graph rather than to produce substantive
output. See `AGENTS.md` Section 3.

## Cross-tool layout

The same agents and skills serve both Claude Code and Google
Antigravity. `.claude/` is the canonical store; `scripts/sync-agents.py`
mirrors `.claude/agents/` to `.agents/` (Antigravity's expected path).
`.mcp.json` and `.antigravity/mcp.json` are identical and both
enumerate the 27 MCP servers in `mcp-servers/`.

## Hard gates

`hard-gate-keeper` is the only non-bypassable agent. Any specialist
whose output triggers a hard-gate-list item (Section 4 of AGENTS.md)
must hand to `hard-gate-keeper` before release. The keeper waits for
explicit operator approval ("approve" or "release") before letting
the deliverable out.



## 4. Multi-jurisdiction routing

```
user ──► task-router ──► jurisdiction-detector ──► jurisdictional specialist set
                              │
                              ├── cn-* (existing flat tree under .claude/agents/<area>/)
                              ├── sg-* (under .claude/agents/singapore/)
                              ├── us-* (under .claude/agents/us/)
                              └── cross-border-* (under .claude/agents/cross-border/)
```

`task-router` runs detection first, picks a single jurisdiction or
cross-border specialist, then dispatches with a brief that explicitly
names the governing law. Specialists hand off to `doc-ops` for formatting
per the chosen jurisdiction's style (CN per GB/T 9704—2012, SG per SAL
Style Guide, US per Bluebook).

MCP servers are namespaced: `sg-*` under `mcp-servers/singapore/`, `us-*`
under `mcp-servers/us/`, CN servers retain the existing flat layout under
`mcp-servers/<name>/`.
