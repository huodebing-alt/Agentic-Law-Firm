# MCP server: Google Calendar

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `gcal-stub`. Exposes one tool
(`gcal_call`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires Calendar API + OAuth.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/gcal-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
