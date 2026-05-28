---
name: contract-review-cn
description: Review a Chinese-language contract: risk, missing clauses, compliance gaps. Use when the user uploads a contract or says '审一下'.
---

# Contract Review (Chinese-language)

## Inputs
- Path to contract file (.docx, .pdf)
- Party role (买方 / 卖方 / 甲方 / 乙方)
- Risk preference

## Workflow
1. Extract text via doc-ops-text-extraction
2. Identify contract type
3. Run the type-specific checklist
4. Flag missing / one-sided clauses / compliance risks
5. Generate review memo per legal-memo-cn.docx template
6. Optionally generate redline via doc-ops-redline

## Output
Review memo .docx + optional redline .docx.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
