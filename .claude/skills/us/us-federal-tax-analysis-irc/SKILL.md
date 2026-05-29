---
name: us-federal-tax-analysis-irc
description: Apply an IRC section to a transaction.
---

# Us Federal Tax Analysis Irc

## Inputs
- Transaction description
- Code section

## Workflow
1. Pull IRC section and Treas Reg via us-cornell-lii
2. Apply leading cases via us-courtlistener
3. Output tax memo

## Output
Federal tax memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
