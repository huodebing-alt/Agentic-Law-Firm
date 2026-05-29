---
name: sg-tax-treaty-application
description: Apply a SG DTAA for inbound / outbound payments (interest, royalty, dividend, services).
---

# Sg Tax Treaty Application

## Inputs
- Counterparty country
- Income type and amount

## Workflow
1. Identify applicable DTAA article
2. Run beneficial-ownership and substance check
3. Apply withholding rate and IRAS S45 procedures
4. Draft Certificate of Residence application if outbound
5. Output treaty memo

## Output
DTAA application memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
