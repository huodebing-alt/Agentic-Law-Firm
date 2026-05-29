---
name: sg-sfa-licensing-analysis
description: Decide if an activity needs a CMS licence under SFA Part 4 or other MAS licensing.
---

# Sg Sfa Licensing Analysis

## Inputs
- Activity description
- Counterparties and product

## Workflow
1. Map activity to regulated activity in SFA Second Schedule
2. Check exemptions (AI/II, related corporation)
3. Identify CMS licence class and capital
4. Output licensing memo

## Output
CMS licensing memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
