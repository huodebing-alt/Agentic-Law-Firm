---
name: sg-acra-bizfile-search
description: Search ACRA BizFile+ for a Singapore company's registered details, officers, charges.
---

# Sg Acra Bizfile Search

## Inputs
- UEN or company name

## Workflow
1. Hit sg-acra-bizfile lookup_company
2. Pull officers, registered address, charges, capital
3. Cross-check against BO register if accessible
4. Output structured profile

## Output
Company profile JSON plus narrative summary.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
