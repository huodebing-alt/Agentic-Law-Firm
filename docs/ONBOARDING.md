# Onboarding

First-time setup runs through the `/onboard` (or `/start`) slash
command. The command loads `.claude/commands/onboard.md`, which
routes to the `onboarding-host` agent at
`.claude/agents/onboarding/onboarding-host.md`. The agent collects
five answers and then calls `scripts/onboard.py` via the Bash tool.

## The five questions

1. **Practice area** — `corporate` / `individual` / `both`. Controls
   which specialist agents and skills are emphasised in `task-router`.
2. **MCP install** — `all` / `select` / `none`. Calls
   `scripts/install-mcp.py` with the chosen list.
3. **Statute library** — `all` / `select` / `none`. Calls
   `scripts/prepare-statutes.py` to download the chosen statutes from
   the `statutes/manifest.json` list.
4. **Hard gates** — `yes` / `no`. Sets `hard_gates.enabled` and
   `hard_gates.deal_value_threshold` (default RMB 100,000,000).
5. **Identity** — `solo` / `firm` / `in-house` / `learning`. Used by
   `task-router` to shape its triage style.

The answers are written to `.agentic-law-firm-config.json` at the
project root. The file looks like:

```json
{
  "practice_area": "both",
  "mcp_install": "all",
  "statutes": "all",
  "hard_gates": {
    "enabled": true,
    "deal_value_threshold": 100000000,
    "currency": "CNY"
  },
  "identity": "solo",
  "language": "zh-CN",
  "matters": []
}
```

Re-running `/onboard` re-prompts with current values pre-filled.
