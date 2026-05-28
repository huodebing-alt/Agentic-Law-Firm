# MCP server: SAMR (国家市场监督管理总局)

Status: **stub** (returns mock data).

## What it is
A minimal MCP server stub for `samr`. Exposes one tool
(`samr_lookup`) that currently returns a static mock response so
the harness can boot.

## How to wire the real backend
Scrape samr.gov.cn 反垄断局 + 市场秩序司 publication lists, or use a paid aggregator.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/samr/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
