# MCP server: Slack

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `slack-stub`. Exposes one tool
(`slack_call`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a Slack app with the needed scopes.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/slack-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
