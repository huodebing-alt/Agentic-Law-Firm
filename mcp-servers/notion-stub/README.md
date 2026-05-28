# MCP server: Notion

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `notion-stub`. Exposes one tool
(`notion_call`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a Notion internal integration and the page sharing.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/notion-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
