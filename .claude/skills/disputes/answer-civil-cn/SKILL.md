---
name: answer-civil-cn
description: Draft a PRC civil defence (民事答辩状).
---

# PRC Civil Defence

## Inputs
- Complaint
- Defence theory

## Workflow
1. Parse the complaint
2. Draft 答辩状 per court rules
3. Add counterclaim if applicable
4. Format per style guide
5. Hand to hard-gate-keeper

## Output
答辩状 .docx.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
