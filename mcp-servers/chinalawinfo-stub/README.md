# MCP server: ChinaLawInfo (北大法意)

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `chinalawinfo-stub`. Exposes one tool
(`chinalawinfo_search`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Requires a subscription. Wire via chinalawinfo.com authenticated session.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/chinalawinfo-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
