# MCP server: e-Sign (e签宝)

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `esign-stub`. Exposes one tool
(`esign_send`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires an e签宝 enterprise account. Wire via open.esign.cn.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/esign-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
