---
name: onboard
description: First-time setup wizard. Walks through jurisdiction, practice areas, MCP install, statute library, hard gates, and identity.
---

# /onboard

Run the onboarding wizard. The host agent does the following, in order.

### Step 0 — environment checks (always)

Before asking any questions, the host runs these Bash commands and aborts with a clear message if any of them fail:

```bash
python3 -c "import sys; assert sys.version_info >= (3, 10), sys.version"
python3 -m pip --version
```

If either check fails, the host stops and tells the user to follow Section 2 (Prerequisites) of the README. **It does not proceed to the questions.**

### Step 1 — install MCP server dependencies (always)

```bash
bash scripts/install-mcp-deps.sh
```

This creates `.venv`, installs `requirements.txt`, `mcp-servers/requirements.txt`, and every `mcp-servers/*/requirements.txt`. **Skipping this step is the single most common cause of "MCP server failed to start" errors.**

### Step 2 — questions

1. **Jurisdictions** — which of the supported jurisdictions to enable. Options: `cn` (China), `sg` (Singapore), `us` (United States), `cross-border`, `all`. Default: `all`.
2. **Practice areas** — free-text, mapped against the routing matrix.
3. **MCP selection** — `all`, a comma-separated subset, or `none`. The wizard only lists MCPs relevant to the jurisdictions chosen above.
4. **Statute library** — `all`, a selection, or `none`. CN has 17 statutes, SG has 16, US has 12 items (USC titles + DGCL + state codes).
5. **Hard gates** — `yes` (default) or `no`. With `yes`, the wizard asks for the deal-value threshold above which `hard-gate-keeper` pauses.
6. **Identity** — `solo` / `firm` / `in-house` / `learning`.

### Step 3 — wire it up

```bash
python3 scripts/onboard.py \
  --jurisdictions=<list> --mcps=<list> --statutes=<list> \
  --hard-gates=<yes|no> --identity=<role>
```

### Step 4 — verify MCP servers can launch

```bash
bash scripts/test-mcp.sh
```

If any server prints `[FAIL]`, the host shows the traceback and tells the user which dependency or API key is missing. It then suggests re-running `bash scripts/install-mcp-deps.sh` and links to that server's own README.

### Step 5 — confirm and suggest next step

The host prints a one-line summary (jurisdictions / MCPs / statutes / hard-gates / identity) and recommends one starting skill that fits the user's jurisdiction and identity (e.g. `china/contract-review-cn` for a CN solo lawyer).

Re-run `/onboard` any time to reconfigure.

## /onboard 中文版

引导向导按顺序执行：

**第 0 步 — 环境检查（必做）**：检查 Python ≥ 3.10 与 pip 可用，失败则提示用户照 README 第 2 节 Prerequisites 安装，并停止。

**第 1 步 — 安装 MCP 依赖（必做）**：`bash scripts/install-mcp-deps.sh`。这一步若跳过，所有本地 MCP server 启动都会失败。

**第 2 步 — 询问**：

1. 执业司法管辖区：cn / sg / us / cross-border / all（默认 all）
2. 业务领域（自由文本）
3. MCP 安装：all / 勾选 / none（仅显示所选 jurisdiction 相关 MCP）
4. 法规库：CN 17 部 / SG 16 部 / US 12 项，可全选 / 勾选 / 不下载
5. hard-gate：开 / 关，开时设定金额阈值
6. 身份：单飞 / 律所 / 法务 / 学习

**第 3 步 — 写配置**：调 `python3 scripts/onboard.py`。

**第 4 步 — 验证 MCP**：`bash scripts/test-mcp.sh`，逐个测试 server import 是否通过。失败时显示具体 traceback 与对应 server 的 README 链接。

**第 5 步 — 完成**：输出一行摘要，并推荐第一个可试的 skill。

任何时候都可以重跑 `/onboard`。
