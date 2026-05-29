---
name: onboard
description: First-time setup wizard. Walks through jurisdiction, practice areas, MCP install, statute library, hard gates, and identity.
---

# /onboard

Run the onboarding wizard. The host agent will ask:

1. **Jurisdictions** — which of the supported jurisdictions you want to enable.
   Options: `cn` (China), `sg` (Singapore), `us` (United States), `cross-border`,
   `all`. Default: `all`.
2. **Practice areas** — free-text, mapped against the routing matrix.
3. **MCP install** — `all`, a selection, or `none`. The wizard will only show
   MCPs relevant to the jurisdictions you chose in step 1.
4. **Statute library** — `all`, a selection, or `none`. CN has 17 statutes,
   SG has 16, US has 12 items (USC titles + DGCL + state codes).
5. **Hard gates** — `yes` (default) or `no`. With `yes`, the wizard asks
   for the deal-value threshold above which `hard-gate-keeper` will pause.
6. **Identity** — `solo` / `firm` / `in-house` / `learning`.

After the answers are collected, the wizard runs:

```bash
python3 scripts/onboard.py --jurisdictions=<list> [--mcps=<list>] [--statutes=<list>]
```

Re-run `/onboard` any time to reconfigure.

## /onboard 中文版

引导向导依次询问：

1. **执业司法管辖区**：cn / sg / us / cross-border / all。默认 all。
2. **业务领域**：自由文本。
3. **MCP 安装**：all / 勾选 / none，列表仅显示所选 jurisdiction 相关的 MCP。
4. **法规库**：CN 17 部 / SG 16 部 / US 12 项，可全选 / 勾选 / 不下载。
5. **hard-gate**：开 / 关，开时设定金额阈值。
6. **身份**：单飞 / 律所 / 法务 / 学习。

任何时候都可以重跑 `/onboard`。
