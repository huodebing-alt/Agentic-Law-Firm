---
name: us-edgar-form4-monitoring
description: Monitor Form 4 insider transactions for an issuer.
---

# Us Edgar Form4 Monitoring

## Inputs
- Issuer CIK

## Workflow
1. Pull Form 4 via us-sec-edgar
2. Aggregate insider transactions
3. Output Form 4 monitoring memo

## Output
Form 4 monitoring memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
