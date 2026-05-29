# MCP server: sg-lawnet

Status: **stub**.

## What it is
A minimal MCP server stub for `sg-lawnet`. LawNet (lawnet.sg) — subscription. SG case law and Singapore Law Reports.

## How to wire the real backend
Requires LawNet subscription. Plug paid credentials and use their case API or HTML scraping under licence terms.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/singapore/lawnet/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
