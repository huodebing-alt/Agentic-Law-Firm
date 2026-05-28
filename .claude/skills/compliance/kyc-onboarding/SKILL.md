---
name: kyc-onboarding
description: Run KYC on a new customer counter-party.
---

# KYC Onboarding

## Inputs
- Customer name
- Activity
- Geography

## Workflow
1. Pull tianyancha / qichacha / samr / sanctions
2. Run beneficial-ownership trace
3. Score risk tier
4. Draft file note
5. Output package

## Output
KYC file note.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
