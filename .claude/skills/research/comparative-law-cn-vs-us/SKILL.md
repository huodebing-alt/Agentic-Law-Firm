---
name: comparative-law-cn-vs-us
description: Build a comparative-law memo (PRC vs US) on a specific topic.
---

# Comparative Law (CN vs US)

## Inputs
- Topic
- Use case

## Workflow
1. Pull PRC position (statutes-rag / wenshu)
2. Pull US position (westlaw)
3. Build side-by-side comparison
4. Identify divergence and operational implications
5. Output memo

## Output
Comparative-law memo.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
