# Extending MCP connectors

Each MCP server under `mcp-servers/<name>/` is a stub: it boots
cleanly, returns mock data, and contains a `README.md` describing
the real backend.

## Typical wiring steps

1. Get API credentials from the provider.
2. Decide a credential storage strategy — environment variables
   (simplest, matches MCP convention) or a local secrets file
   (`.agentic-law-firm-secrets.json`, in `.gitignore`).
3. Replace the body of the tool function in `server.py` with real
   HTTP calls.
4. Keep the tool signature the same so agents and skills do not
   need to be re-written.
5. Run `scripts/test-mcp.sh <name>` to round-trip a call.
6. Commit the change in a branch and run `scripts/verify.sh`.

## Adding a new MCP

1. `mkdir mcp-servers/my-new-mcp`
2. Copy the structure of an existing stub.
3. Add an entry to both `.mcp.json` and `.antigravity/mcp.json`.
4. Add an entry to `docs/MCP_CATALOG.md`.
5. If an agent should call it, add it to the agent's `MCP
   dependencies` block.
6. Run `scripts/verify.sh`.

## Notes on PRC data sources

- The `国家法律法规数据库` (flk.npc.gov.cn) is the only fully open
  official source for current PRC statutes. PKULaw and WKInfo
  provide better consolidation and history but require subscription.
- 裁判文书网 (wenshu) tightened access in 2024; the stub does not
  attempt to scrape. Recommended: use a paid aggregator (e.g.
  Alpha 法律智能操作系统, Lawsdata) or a snapshot.
- SAMR and CNIPA publish much of their data on their official
  websites without authentication, but rate-limit aggressively.
