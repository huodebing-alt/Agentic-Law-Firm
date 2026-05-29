# MCP server: sg-ipos

Status: **stub**.

## What it is
A minimal MCP server stub for `sg-ipos`. Intellectual Property Office of Singapore (ipos.gov.sg). Trademark / patent / design / copyright search.

## How to wire the real backend
Use the IP2SG public search APIs or scrape ipos.gov.sg's eSearch.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/singapore/ipos/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
