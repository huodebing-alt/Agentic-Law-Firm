---
name: annual-compliance-calendar
description: Build the annual compliance calendar for a PRC entity.
---

# Annual Compliance Calendar

## Inputs
- Entity profile

## Workflow
1. Pull all recurring obligations (SAMR, MOFCOM, tax, social, FX)
2. Sequence by month
3. Add owners and reminders
4. Output calendar .docx

## Output
Annual compliance calendar .docx.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
