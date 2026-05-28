---
name: contract-review-en
description: Review an English-language contract under common-law style.
---

# Contract Review (English)

## Inputs
- Path to contract file
- Party role
- Counter-party leverage

## Workflow
1. Extract text
2. Identify contract type
3. Run common-law checklist
4. Flag enforceability under PRC law if PRC party
5. Output review memo

## Output
Review memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
