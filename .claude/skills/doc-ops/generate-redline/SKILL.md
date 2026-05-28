---
name: generate-redline
description: Apply tracked-changes edits between original and revised .docx.
---

# Generate Redline

## Inputs
- Original .docx
- Revised .docx or change list

## Workflow
1. Load both
2. Apply edits as tracked changes
3. Format per style guide
4. Output redline .docx
5. Append change log

## Output
Redline .docx + change log.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
