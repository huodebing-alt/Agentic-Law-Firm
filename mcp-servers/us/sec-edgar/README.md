# MCP server: us-sec-edgar

Status: **stub**.

## What it is
A minimal MCP server stub for `us-sec-edgar`. SEC EDGAR (sec.gov/edgar). Public-company filings.

## How to wire the real backend
Use EDGAR's public REST endpoints at https://data.sec.gov/. No auth required, throttle to 10 req/s.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/us/sec-edgar/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
