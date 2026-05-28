---
name: trademark-search-cn
description: Run a CNIPA trademark availability search and produce a clearance memo.
---

# Trademark Search (CNIPA)

## Inputs
- Mark
- Classes

## Workflow
1. Query CNIPA via cnipa MCP
2. Cluster results
3. Flag conflicts and risks
4. Output clearance memo
5. Hand to trademark-cn

## Output
Clearance memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
