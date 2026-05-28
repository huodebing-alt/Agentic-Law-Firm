# MCP server: NetDocuments

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `netdocuments-stub`. Exposes one tool
(`netdocs_search`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a NetDocuments cabinet and OAuth app.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/netdocuments-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
