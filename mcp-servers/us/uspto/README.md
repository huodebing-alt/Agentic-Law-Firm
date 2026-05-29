# MCP server: us-uspto

Status: **stub**.

## What it is
A minimal MCP server stub for `us-uspto`. USPTO TSDR (trademarks) and PatentsView (patents). Free public APIs.

## How to wire the real backend
Use TSDR REST at https://tsdr.uspto.gov/ and PatentsView at https://search.patentsview.org/.

## How to run the stub
```bash
pip install mcp
python3 mcp-servers/us/uspto/server.py
```

The harness picks this server up via `.mcp.json` (Claude Code)
and `.antigravity/mcp.json` (Antigravity).
