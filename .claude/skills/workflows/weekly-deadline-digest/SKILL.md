---
name: weekly-deadline-digest
description: Produce a weekly digest of all upcoming deadlines across active matters.
---

# Weekly Deadline Digest

## Inputs
- .agentic-law-firm-config.json

## Workflow
1. Pull deadlines from active matters
2. Sort by urgency
3. Add suggested actions per item
4. Output digest .docx / Markdown

## Output
Weekly deadline digest.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
