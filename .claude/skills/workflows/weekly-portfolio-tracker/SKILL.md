---
name: weekly-portfolio-tracker
description: Build a weekly tracker for the operator's matters: status, deadlines, next actions.
---

# Weekly Portfolio Tracker

## Inputs
- .agentic-law-firm-config.json matters[]

## Workflow
1. Pull active matters
2. Compute deadlines and overdue items
3. Draft next-action list per matter
4. Output weekly status memo

## Output
Weekly status memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
