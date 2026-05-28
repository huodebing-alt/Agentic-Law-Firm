# MCP server: QiChaCha (企查查)

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `qichacha-stub`. Exposes one tool
(`qcc_company`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a QiChaCha API key. Wire via openapi.qcc.com.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/qichacha-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
