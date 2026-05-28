# MCP server: OneDrive

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `onedrive-stub`. Exposes one tool
(`onedrive_call`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Use the same M365 app reg with Files.ReadWrite scope.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/onedrive-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
