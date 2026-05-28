---
name: matter-status-report
description: Build a per-matter status report for a partner / client.
---

# Matter Status Report

## Inputs
- Matter id from config

## Workflow
1. Pull all activity since the last report
2. Summarise progress, blockers, next actions
3. Format per style guide
4. Output .docx

## Output
Matter status report .docx.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
