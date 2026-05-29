# MCP server: sg-singapore-law-watch

Status: **stub**.

## What it is
A minimal MCP server stub for `sg-singapore-law-watch`. Singapore Law Watch (singaporelawwatch.sg). Daily SG legal news headlines.

## How to wire the real backend
Scrape the daily highlights RSS / HTML feed.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/singapore/singapore-law-watch/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
