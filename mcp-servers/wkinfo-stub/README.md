# MCP server: WKInfo (威科先行)

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `wkinfo-stub`. Exposes one tool
(`wkinfo_search`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a subscription. Wire via wkinfo.com.cn authenticated session.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/wkinfo-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
