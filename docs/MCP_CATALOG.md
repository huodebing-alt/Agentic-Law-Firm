# MCP Catalogue

- **statutes-rag** (Statutes RAG) — status: `stub` — tool: `lookup_statute`
- **wenshu** (China Judgment Documents (裁判文书网)) — status: `stub` — tool: `search_judgments`
- **samr** (SAMR (国家市场监督管理总局)) — status: `stub` — tool: `samr_lookup`
- **cnipa** (CNIPA (国家知识产权局)) — status: `stub` — tool: `cnipa_search`
- **pkulaw-stub** (PKULaw (北大法宝)) — status: `stub` — tool: `pkulaw_search`
- **wkinfo-stub** (WKInfo (威科先行)) — status: `stub` — tool: `wkinfo_search`
- **chinalawinfo-stub** (ChinaLawInfo (北大法意)) — status: `stub` — tool: `chinalawinfo_search`
- **westlaw-stub** (Westlaw) — status: `stub` — tool: `westlaw_search`
- **lexisnexis-stub** (LexisNexis) — status: `stub` — tool: `lexis_search`
- **tianyancha-stub** (TianYanCha (天眼查)) — status: `stub` — tool: `tyc_company`
- **qichacha-stub** (QiChaCha (企查查)) — status: `stub` — tool: `qcc_company`
- **fadada-stub** (FaDaDa (法大大)) — status: `stub` — tool: `fdd_send`
- **esign-stub** (e-Sign (e签宝)) — status: `stub` — tool: `esign_send`
- **imanage-stub** (iManage) — status: `stub` — tool: `imanage_search`
- **netdocuments-stub** (NetDocuments) — status: `stub` — tool: `netdocs_search`
- **ms365-stub** (Microsoft 365) — status: `stub` — tool: `m365_call`
- **gmail-stub** (Gmail) — status: `stub` — tool: `gmail_call`
- **gdrive-stub** (Google Drive) — status: `stub` — tool: `gdrive_call`
- **gcal-stub** (Google Calendar) — status: `stub` — tool: `gcal_call`
- **onedrive-stub** (OneDrive) — status: `stub` — tool: `onedrive_call`
- **sharepoint-stub** (SharePoint) — status: `stub` — tool: `sharepoint_call`
- **box-stub** (Box) — status: `stub` — tool: `box_call`
- **dropbox-stub** (Dropbox) — status: `stub` — tool: `dropbox_call`
- **notion-stub** (Notion) — status: `stub` — tool: `notion_call`
- **slack-stub** (Slack) — status: `stub` — tool: `slack_call`
- **zoom-stub** (Zoom) — status: `stub` — tool: `zoom_call`
- **teams-stub** (Microsoft Teams) — status: `stub` — tool: `teams_call`



## Singapore (8)

- `sg-sso-statutes` — Singapore Statutes Online (sso.agc.gov.sg) text lookup.
- `sg-acra-bizfile` — ACRA BizFile+ company profile / officers / charges.
- `sg-ipos` — IPOS trademark / patent / design / copyright search.
- `sg-iras` — IRAS e-Tax Guides, advance rulings, GST register.
- `sg-lawnet` — LawNet (subscription) SG case-law search.
- `sg-singapore-law-watch` — Daily SG legal news headlines.
- `sg-mas-public` — MAS Notices, Guidelines, FI register.
- `sg-sicc-siac` — SICC + SIAC rules and cause lists.

## United States (5)

- `us-cornell-lii` — Cornell LII USC / CFR / FRCP / state code lookup.
- `us-courtlistener` — CourtListener / Free Law Project case-law search.
- `us-sec-edgar` — SEC EDGAR public-company filings.
- `us-uspto` — USPTO TSDR (trademarks) + PatentsView (patents).
- `us-pacer-stub` — PACER federal dockets (subscription, stub).

## Real-API readiness

| Server | Status | Real-API path |
|---|---|---|
| sg-sso-statutes | stub | Public HTML scrape of sso.agc.gov.sg |
| sg-acra-bizfile | stub | Paid BizFile+ API or HTML scrape of public profile |
| sg-ipos | stub | IP2SG public search HTML / undocumented API |
| sg-iras | stub | Public HTML scrape of iras.gov.sg |
| sg-lawnet | stub | Subscription required |
| sg-singapore-law-watch | stub | Public HTML scrape |
| sg-mas-public | stub | Public HTML scrape of mas.gov.sg |
| sg-sicc-siac | stub | Public HTML scrape |
| us-cornell-lii | stub | Public-domain HTML scrape, no auth |
| us-courtlistener | stub | Free-tier REST v4 API, free API key |
| us-sec-edgar | stub | Public REST at data.sec.gov, throttle 10 r/s |
| us-uspto | stub | TSDR + PatentsView, both free |
| us-pacer-stub | stub | PACER pay-per-page subscription |
