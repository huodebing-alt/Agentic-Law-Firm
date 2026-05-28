# MCP server: iManage

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `imanage-stub`. Exposes one tool
(`imanage_search`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires an iManage Cloud / on-prem instance and an OAuth app.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/imanage-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
