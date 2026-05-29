---
name: us-hsr-filing-analysis
description: Decide if an HSR filing is required.
---

# Us Hsr Filing Analysis

## Inputs
- Transaction value
- Sizes of person

## Workflow
1. Apply 2026 HSR thresholds
2. Apply size-of-transaction and size-of-person tests
3. Identify exemptions (16 CFR 802)
4. Output HSR memo

## Output
HSR memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
