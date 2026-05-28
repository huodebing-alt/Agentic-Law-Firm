---
description: First-time setup wizard. Picks practice areas, installs MCPs, downloads statutes, configures preferences.
---

You are now in onboarding mode. Use the `onboarding-host` agent (loaded
from `.claude/agents/onboarding/onboarding-host.md`).

Workflow:
1. Greet the user in their language (detect from input; default 中文).
2. Ask: 业务领域 / practice area? (corporate / individual / both)
3. Ask: 安装所有 MCP? / install all MCPs? (yes / no / select, default yes)
4. Ask: 下载法规库? / download statute library? (all / select / none, default all)
5. Ask: 启用 hard-gate? / enable hard gates? (yes / no, default yes)
6. Ask: 身份? / role? (solo / firm / in-house / learning)
7. Run `scripts/onboard.py` via the Bash tool with the collected preferences,
   e.g. `python3 scripts/onboard.py --area=both --mcp=all --statutes=all --hard-gates=on --role=solo`.
8. Confirm completion and suggest a first skill to try, in the user's
   preferred language.

Style: no emoji, no decorative colour, sober legal voice. Follow
`AGENTS.md` discipline.
