# MCP server: Zoom

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `zoom-stub`. Exposes one tool
(`zoom_call`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a Zoom app with the needed scopes.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/zoom-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
