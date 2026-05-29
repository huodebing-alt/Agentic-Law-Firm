# MCP server: us-courtlistener

Status: **stub**.

## What it is
A minimal MCP server stub for `us-courtlistener`. CourtListener / Free Law Project (courtlistener.com). US case law search and PACER docket integration.

## How to wire the real backend
Use CourtListener REST API v4 at https://www.courtlistener.com/api/rest/v4/; free tier with API key.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/us/courtlistener/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
