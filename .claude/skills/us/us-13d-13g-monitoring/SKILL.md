---
name: us-13d-13g-monitoring
description: Monitor 13D/G filings for a target issuer.
---

# Us 13D 13G Monitoring

## Inputs
- Issuer name or CIK

## Workflow
1. Pull 13D/G via us-sec-edgar
2. Compute beneficial-ownership thresholds
3. Flag amendment triggers
4. Output monitoring memo

## Output
13D/G monitoring memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
