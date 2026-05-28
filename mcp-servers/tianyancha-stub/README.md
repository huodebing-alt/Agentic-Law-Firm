# MCP server: TianYanCha (天眼查)

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `tianyancha-stub`. Exposes one tool
(`tyc_company`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a TianYanCha API key. Wire via open.tianyancha.com.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/tianyancha-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
