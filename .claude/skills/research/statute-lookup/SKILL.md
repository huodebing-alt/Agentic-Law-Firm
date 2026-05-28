---
name: statute-lookup
description: Look up PRC statute / regulation / judicial interpretation by topic or citation.
---

# Statute Lookup

## Inputs
- Topic or citation

## Workflow
1. Query statutes-rag
2. Filter by hierarchy and effective date
3. Return citation-ready references
4. Hand to requesting specialist

## Output
Statute citations.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely.

## References
- statutes-rag MCP
- pkulaw-stub / wkinfo-stub
