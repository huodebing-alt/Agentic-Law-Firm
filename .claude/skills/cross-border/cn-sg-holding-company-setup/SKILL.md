---
name: cn-sg-holding-company-setup
description: Set up a SG holding company for a CN operating group.
---

# Cn Sg Holding Company Setup

## Inputs
- Group structure
- Tax goals

## Workflow
1. Apply CN outbound: ODI (MOFCOM), SAFE, NDRC
2. Apply SG: ACRA incorporation, MAS notification if FS, substance test
3. Apply CN-SG DTAA for dividend / interest / royalty
4. Output structuring memo

## Output
CN-SG holding memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
