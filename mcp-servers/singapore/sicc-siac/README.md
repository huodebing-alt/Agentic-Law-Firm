# MCP server: sg-sicc-siac

Status: **stub**.

## What it is
A minimal MCP server stub for `sg-sicc-siac`. SICC (sicc.gov.sg) and SIAC (siac.org.sg). Cause lists, awards summaries, rules.

## How to wire the real backend
Scrape SIAC and SICC official sites; only public documents are accessible.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/singapore/sicc-siac/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
