---
name: extract-text
description: Extract text (with structure) from a docx / pdf / scanned-pdf / doc / rtf.
---

# Text Extraction

## Inputs
- File path

## Workflow
1. Detect file type
2. Use python-docx / pdfplumber / OCR
3. Preserve heading structure
4. Emit Markdown
5. Hand to requesting agent

## Output
Markdown text.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
