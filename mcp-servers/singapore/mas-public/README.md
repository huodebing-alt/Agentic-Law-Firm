# MCP server: sg-mas-public

Status: **stub**.

## What it is
A minimal MCP server stub for `sg-mas-public`. Monetary Authority of Singapore public data (mas.gov.sg). Notices, guidelines, FI register.

## How to wire the real backend
Scrape mas.gov.sg's regulations and FI register pages.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/singapore/mas-public/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
