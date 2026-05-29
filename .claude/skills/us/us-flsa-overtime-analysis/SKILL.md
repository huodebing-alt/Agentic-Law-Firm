---
name: us-flsa-overtime-analysis
description: Decide FLSA exempt / non-exempt status for a role.
---

# Us Flsa Overtime Analysis

## Inputs
- Role, duties, salary

## Workflow
1. Apply salary basis and salary-level tests
2. Apply duties test (executive, administrative, professional)
3. Apply state overlay (CA, NY)
4. Output FLSA memo

## Output
FLSA classification memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
