---
name: us-10k-extraction
description: Extract risk factors, MD&A, and contingencies from a 10-K.
---

# Us 10K Extraction

## Inputs
- 10-K URL or text

## Workflow
1. Hit us-sec-edgar fetch_filing
2. Extract Items 1A, 7, 8-Note Litigation
3. Output structured summary

## Output
10-K extraction memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
