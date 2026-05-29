# MCP server: sg-sso-statutes

Status: **stub**.

## What it is
A minimal MCP server stub for `sg-sso-statutes`. Singapore Statutes Online (sso.agc.gov.sg). Returns Acts and subsidiary legislation by short title or section.

## How to wire the real backend
Scrape https://sso.agc.gov.sg/ HTML or use the official JSON feed if available; cache locally.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/singapore/sso-statutes/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
