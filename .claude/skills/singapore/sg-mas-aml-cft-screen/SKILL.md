---
name: sg-mas-aml-cft-screen
description: Run an AML/CFT screen for a SG financial institution per MAS Notice 626 / 824 / 1014.
---

# Sg Mas Aml Cft Screen

## Inputs
- Customer profile
- Transactions

## Workflow
1. Apply CDD/EDD per relevant MAS notice
2. Map STR triggers and SAR escalation
3. Output AML screen memo

## Output
AML screen memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
