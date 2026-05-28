---
name: westlaw-search
description: Search Westlaw for foreign law (US / UK / EU).
---

# Westlaw Search

## Inputs
- Jurisdiction
- Topic

## Workflow
1. Query westlaw-stub
2. Filter by jurisdiction and date
3. Summarise the points of law
4. Hand to requesting specialist

## Output
Foreign-law citations + summary.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
