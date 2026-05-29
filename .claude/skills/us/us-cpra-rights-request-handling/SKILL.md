---
name: us-cpra-rights-request-handling
description: Process a CPRA consumer rights request (know, delete, correct, opt-out).
---

# Us Cpra Rights Request Handling

## Inputs
- Request type
- Consumer verification

## Workflow
1. Verify consumer identity
2. Pull data inventory and run extraction
3. Apply exemptions
4. Draft response and update opt-out preference signal handling
5. Output response packet

## Output
CPRA response packet.

Every client-facing document follows `docs/DOCUMENT_STYLE_GUIDE.md`.
No emoji. No decorative colour. Black on white. Cite statutes and
cases precisely per jurisdiction convention.

## References
- `AGENTS.md`
- `docs/DOCUMENT_STYLE_GUIDE.md`
- `docs/JURISDICTION_GUIDE.md`
