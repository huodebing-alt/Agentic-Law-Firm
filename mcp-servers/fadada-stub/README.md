# MCP server: FaDaDa (法大大)

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `fadada-stub`. Exposes one tool
(`fdd_send`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a FaDaDa enterprise account. Wire via open.fadada.com.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/fadada-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
