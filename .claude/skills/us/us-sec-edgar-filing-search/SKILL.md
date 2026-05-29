---
name: us-sec-edgar-filing-search
description: Search SEC EDGAR for a filer's filings.
---

# Us Sec Edgar Filing Search

## Inputs
- Filer name or CIK

## Workflow
1. Hit us-sec-edgar lookup_filings
2. Return list of filings with type / date / URL
3. Output filings index

## Output
SEC filings index.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
