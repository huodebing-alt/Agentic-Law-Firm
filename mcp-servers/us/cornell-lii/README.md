# MCP server: us-cornell-lii

Status: **stub**.

## What it is
A minimal MCP server stub for `us-cornell-lii`. Cornell Law - Legal Information Institute (law.cornell.edu). USC, CFR, FRCP, state codes.

## How to wire the real backend
Scrape law.cornell.edu pages; LII content is public-domain government text.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/us/cornell-lii/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
