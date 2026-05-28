# MCP server: Dropbox

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `dropbox-stub`. Exposes one tool
(`dropbox_call`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a Dropbox API app and OAuth.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/dropbox-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
