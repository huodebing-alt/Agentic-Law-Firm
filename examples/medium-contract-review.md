# Example: medium-complexity contract review

User uploads `procurement-master.docx` (a Chinese-language master
purchase agreement with a foreign supplier) and says:
「我是买方，帮我审一份合同，并给我一份红线版。」

Routing:
1. `task-router` identifies: contract review, role=买方, output=memo+redline.
2. Dispatches to `contract-reviewer-cn` agent.
3. `contract-reviewer-cn` invokes the `contract-review-cn` skill.
4. Skill extracts text via `doc-ops-text-extraction`, identifies it
   as a master purchase / supply agreement, runs the buyer-side
   checklist.
5. `contract-reviewer-cn` produces the review memo, then calls
   `redline-generator` for the redline.
6. `doc-ops-formatter` finalises both deliverables per style guide.
7. `doc-ops-citation-checker` verifies citations.
8. Outputs: `review-memo.docx` and `redline.docx`.

Hard gate: only triggered if the deal value (read from the contract)
exceeds the threshold. If so, `hard-gate-keeper` pauses and asks for
operator approval before releasing the deliverables.

Expected wall-clock time: 2-6 minutes.
