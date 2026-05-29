# MCP server: sg-iras

Status: **stub**.

## What it is
A minimal MCP server stub for `sg-iras`. Inland Revenue Authority of Singapore (iras.gov.sg). Tax guides, advance rulings, GST register.

## How to wire the real backend
Scrape iras.gov.sg knowledge base; for GST register use the public lookup at https://mytax.iras.gov.sg/.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/singapore/iras/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
