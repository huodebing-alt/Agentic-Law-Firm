# MCP server: China Judgment Documents (裁判文书网)

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `wenshu`. Exposes one tool
(`search_judgments`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Replace _stub_response with calls to wenshu.court.gov.cn (note the access controls in 2024+). For PoC, a local SQLite snapshot works.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/wenshu/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
