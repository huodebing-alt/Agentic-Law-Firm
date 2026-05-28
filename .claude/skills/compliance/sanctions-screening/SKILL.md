---
name: sanctions-screening
description: Screen counter-parties and transactions against OFAC / EU / UK / PRC unreliable-entity lists.
---

# Sanctions Screening

## Inputs
- Counter-party list
- Transaction details

## Workflow
1. Pull lists
2. Run name + alias + UBO screening
3. Score risk
4. Recommend mitigations
5. Output screening report

## Output
Screening report.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
