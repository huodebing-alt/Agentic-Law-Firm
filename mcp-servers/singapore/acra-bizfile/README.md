# MCP server: sg-acra-bizfile

Status: **stub**.

## What it is
A minimal MCP server stub for `sg-acra-bizfile`. ACRA BizFile+ (bizfile.gov.sg). Returns SG company / business profiles.

## How to wire the real backend
Use the BizFile+ paid API or scrape the public profile page (limited free info).

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/singapore/acra-bizfile/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
