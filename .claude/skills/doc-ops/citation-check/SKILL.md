---
name: citation-check
description: Verify all statute and case citations against statutes-rag and wenshu.
---

# Citation Check

## Inputs
- Document

## Workflow
1. Extract citations
2. Query statutes-rag and wenshu
3. Flag mismatches and inventions
4. Output a citation-check log

## Output
Citation-check log.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
