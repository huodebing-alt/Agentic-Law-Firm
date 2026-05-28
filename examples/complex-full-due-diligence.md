# Example: complex full M&A due diligence

User: 我们要收购 __________ 公司的 51% 股权，做一份全面尽调，行业是
SaaS，目标在北京，目前没有任何尽调材料。

Routing:
1. `task-router` identifies: full DD, sector=SaaS, jurisdiction=PRC.
2. Recognises scope > 15 sub-tasks. Invokes `task-decomposer`.
3. `task-decomposer` emits a JSON plan with ~60 sub-tasks across:
   corporate (12), contracts (10), employment (8), IP (8), real
   estate (4), tax (8), litigation (6), data-protection (4).
4. Operator approves the plan.
5. `task-router` dispatches in parallel where possible. Specialists
   call MCPs (statutes-rag, wenshu, samr, tianyancha, qichacha,
   cnipa) and feed findings back.
6. `aggregator` composes a single DD report:
   - one-page executive summary
   - risk matrix (red / amber / green)
   - per-area findings sections
   - appendices (contract list, IP list, litigation list, etc.)
7. `doc-ops-formatter` produces the final `.docx`.
8. `hard-gate-keeper` triggers because deal-value is above threshold
   (51% acquisition of a SaaS target). The operator reviews and
   releases.

Expected wall-clock time: 30-90 minutes of agent time, plus operator
review checkpoints at the decomposition step and the hard-gate step.
