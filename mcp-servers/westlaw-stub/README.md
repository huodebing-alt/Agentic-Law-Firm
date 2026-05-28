# MCP server: Westlaw

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `westlaw-stub`. Exposes one tool
(`westlaw_search`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a Thomson Reuters subscription and API access.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/westlaw-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
