---
name: personal-injury-damages-cn
description: Compute PRC personal-injury damages.
---

# PRC Personal Injury Damages

## Inputs
- Injury type
- Medical records
- Income loss

## Workflow
1. Compute medical, lost income, disability, mental anguish
2. Apply local damages schedule
3. Draft damages memo
4. Output memo
5. Hand to personal-injury-cn

## Output
Damages memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
