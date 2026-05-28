# MCP server: Microsoft 365

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `ms365-stub`. Exposes one tool
(`m365_call`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires an Azure AD app registration with Microsoft Graph delegated permissions.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/ms365-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
