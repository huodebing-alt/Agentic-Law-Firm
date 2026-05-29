---
name: sg-gst-registration-analysis
description: Decide GST registration timing and method (compulsory / voluntary, retrospective / prospective).
---

# Sg Gst Registration Analysis

## Inputs
- Taxable turnover by month
- Business model (B2B/B2C, OVR scope)

## Workflow
1. Apply S$1m taxable-turnover threshold
2. Compute retrospective vs prospective basis
3. Check OVR / RC scope for digital services
4. Plan ASK / IGDS / MES if applicable
5. Output registration recommendation

## Output
GST registration memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
