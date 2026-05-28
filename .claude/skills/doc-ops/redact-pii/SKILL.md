---
name: redact-pii
description: Redact PII (and confidential information) from a document.
---

# Redact PII

## Inputs
- Document
- Redaction list

## Workflow
1. Identify PII / confidential terms
2. Apply black-box redactions
3. Output redacted .pdf and a log of redactions

## Output
Redacted .pdf and log.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
