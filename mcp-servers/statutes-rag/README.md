# MCP server: Statutes RAG

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `statutes-rag`. Exposes one tool
(`lookup_statute`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Plug a real backend: PKULaw, WKInfo, ChinaLawInfo, or the official 国家法律法规数据库 (flk.npc.gov.cn).

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/statutes-rag/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
