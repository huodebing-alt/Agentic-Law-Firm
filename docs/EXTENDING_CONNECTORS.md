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



## Singapore data sources

- **sso.agc.gov.sg** — Singapore Statutes Online. HTML only; consult AGC's
  terms before mass scraping.
- **bizfile.gov.sg** — ACRA BizFile+. Paid commercial API for bulk; free
  public profile lookup per UEN.
- **ipos.gov.sg / ip2sg.gov.sg** — IPOS eSearch; HTML scrape.
- **iras.gov.sg** — IRAS e-Tax Guides and Advance Rulings; HTML scrape.
- **lawnet.sg** — Subscription only.
- **singaporelawwatch.sg** — Public RSS / HTML.
- **mas.gov.sg** — MAS Notices, Guidelines, FI register; HTML.
- **sicc.gov.sg / siac.org.sg** — Rules, news, cause lists; HTML.

## United States data sources

- **law.cornell.edu** — Cornell LII. Public-domain government text;
  free; HTML scrape, throttle politely.
- **courtlistener.com** — Free Law Project. REST v4 API at
  /api/rest/v4/, free key, generous rate limit.
- **data.sec.gov / sec.gov/edgar** — SEC EDGAR. Public REST endpoints,
  no auth, ≤10 r/s, declare user-agent header.
- **tsdr.uspto.gov / search.patentsview.org** — USPTO TSDR (TM REST)
  and PatentsView (patent JSON search). Both free.
- **pacer.uscourts.gov** — PACER. Paid; per-page fee; CASE Locator API.
