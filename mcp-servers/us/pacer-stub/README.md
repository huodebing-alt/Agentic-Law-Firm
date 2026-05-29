# MCP server: us-pacer-stub

Status: **stub**.

## What it is
A minimal MCP server stub for `us-pacer-stub`. PACER (pacer.uscourts.gov) — subscription. Federal court dockets and documents.

## How to wire the real backend
Requires PACER credentials and pay-per-page fees. Use the PACER Case Locator API.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/us/pacer-stub/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
