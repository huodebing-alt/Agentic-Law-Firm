# MCP server: Gmail

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `gmail-stub`. Exposes one tool
(`gmail_call`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a Google Cloud project with Gmail API enabled and OAuth.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/gmail-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
