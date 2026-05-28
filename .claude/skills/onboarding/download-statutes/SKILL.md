---
name: download-statutes
description: Download statute texts into statutes/ per manifest.
---

# Download Statutes

## Inputs
- Statute list

## Workflow
1. Read statutes/manifest.json
2. Filter to selected statutes
3. Download to statutes/data/
4. Verify checksums
5. Output download log

## Output
Download log.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
