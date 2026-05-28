# MCP server: CNIPA (国家知识产权局)

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `cnipa`. Exposes one tool
(`cnipa_search`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Wire to sbj.cnipa.gov.cn for trademarks and pss-system.cponline.cnipa.gov.cn for patents.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/cnipa/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
