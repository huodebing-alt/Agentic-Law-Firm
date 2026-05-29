# Agentic-Law-Firm

> A single operator commanding a virtual law firm.
> 一个人，指挥一整间虚拟律所。

140+ specialist agents, 230+ workflow skills, 40 MCP connectors, 40+ document
templates. Built primarily for Google Antigravity; also runs on Claude Code.
Supports China, Singapore, and United States law plus cross-border (CN-SG, CN-US, SG-US, tri-jurisdiction) matters.

140+ 专家 agent、230+ 工作 skill、40 个 MCP 连接器、40+ 文书模板。主要面向
Google Antigravity，同时兼容 Claude Code。支持中国法、新加坡法、美国法以及跨境业务（中新、中美、新美、三法域协调）。

---

## 1. Introduction

Agentic-Law-Firm is what one lawyer needs to behave like a small firm: a
task-router that triages the matter, specialists for every practice area,
document-ops agents that handle drafting, redlining and formatting, and a
hard-gate keeper that refuses to release sensitive output without your sign-off.
The repo is fully model-agnostic — the same agents and skills run on
Antigravity (Gemini 3 Pro / Claude / GPT-OSS) and on Claude Code.

Agentic-Law-Firm 让一位律师可以像一间小律所一样工作：task-router 接案分流，
每个执业领域配专家 agent，doc-ops agent 负责草拟、批注与排版，hard-gate-keeper
在敏感动作前停下来等你拍板。本仓库与具体模型解耦——同一套 agent 与 skill 既能
在 Antigravity 上跑（Gemini 3 Pro / Claude / GPT-OSS），也能在 Claude Code 上跑。

## 2. Prerequisites

Before running Agentic-Law-Firm you need Python 3.10+, one agent runtime (Claude Code or Google Antigravity), and — if you intend to push back to GitHub — git plus the GitHub CLI. The MCP servers in this repo are local Python processes, so their dependencies must be installed before `claude` or `agy` starts, otherwise every local MCP server will fail to launch.

### Python

```bash
# macOS (Homebrew recommended)
brew install python@3.11

# Linux (Ubuntu / Debian)
sudo apt update && sudo apt install -y python3 python3-pip python3-venv

# Windows
# Download from https://www.python.org/downloads/ or install Python 3.11 from Microsoft Store

# Verify
python3 --version    # should be >= 3.10
pip3 --version
```

### Agent runtime (pick one)

**Option A — Claude Code** (widest model coverage):

```bash
# via npm (requires Node.js >= 18)
npm install -g @anthropic-ai/claude-code

# or one-line installer (macOS / Linux)
curl -fsSL https://claude.ai/install.sh | sh

claude login
claude --version
```

**Option B — Google Antigravity** (the agent-first platform, currently public preview):

```bash
# one-line installer (macOS / Linux / Windows under WSL)
curl -fsSL https://antigravity.google/cli/install.sh | bash

# Add ~/.local/bin to PATH if the installer asks you to, then:
agy           # opens the TUI; authenticate with a Google account on first run
```

If `antigravity.google` is unreachable from your region, the desktop application is also available at `antigravity.google.com/download`.

### Git and GitHub CLI (only needed to push your fork)

```bash
# macOS
brew install git gh

# Linux
sudo apt install -y git
# gh: see https://cli.github.com/manual/installation

gh auth login
```

### Optional

- **uv / pyenv** for managing Python virtual environments (avoids polluting system Python).
- **OCR engines** if you intend to use the doc-ops OCR skill: `brew install tesseract tesseract-lang` on macOS, or `pip install paddleocr` for Chinese-heavy scans.
- **LibreOffice** (`brew install --cask libreoffice`) if you want headless `docx → pdf` conversion.

### 2. 前置依赖

运行 Agentic-Law-Firm 前需要装好 Python 3.10+、一个 agent runtime（Claude Code 或 Google Antigravity），如要推回 GitHub 还需要 git 与 GitHub CLI。本项目所有 MCP server 都是本地 Python 进程，依赖必须在 `claude` 或 `agy` 启动**之前**装好，否则所有本地 MCP server 在 launch 时会失败。

#### Python

```bash
# macOS（推荐 Homebrew）
brew install python@3.11

# Linux（Ubuntu / Debian）
sudo apt update && sudo apt install -y python3 python3-pip python3-venv

# Windows
# 从 https://www.python.org/downloads/ 下载，或在 Microsoft Store 装 Python 3.11

# 验证
python3 --version    # 应 >= 3.10
pip3 --version
```

#### Agent runtime（二选一）

**选项 A —— Claude Code**（模型覆盖最广）：

```bash
# 通过 npm（需要 Node.js >= 18）
npm install -g @anthropic-ai/claude-code

# 或一键脚本（macOS / Linux）
curl -fsSL https://claude.ai/install.sh | sh

claude login
claude --version
```

**选项 B —— Google Antigravity**（agent-first 平台，当前公开预览）：

```bash
# 一键脚本（macOS / Linux / Windows 下的 WSL）
curl -fsSL https://antigravity.google/cli/install.sh | bash

# 若安装器提示，把 ~/.local/bin 加到 PATH，然后：
agy           # 打开 TUI；首次启动用 Google 账号认证
```

如果国内访问 `antigravity.google` 不畅，可改用桌面端：`antigravity.google.com/download`。

#### Git 与 GitHub CLI（推送 fork 时需要）

```bash
# macOS
brew install git gh

# Linux
sudo apt install -y git
# gh 的安装见 https://cli.github.com/manual/installation

gh auth login
```

#### 可选

- **uv / pyenv**：管理 Python 虚拟环境（避免污染系统 Python）。
- **OCR 引擎**：用 doc-ops 的 OCR skill 时需要。macOS 装 `brew install tesseract tesseract-lang`；中文扫描件多可装 `pip install paddleocr`。
- **LibreOffice**：headless `docx → pdf` 转换需要，`brew install --cask libreoffice`。

## 3. Quickstart

Run the prerequisites in Section 2 first. Then:

```bash
git clone https://github.com/huodebing-alt/Agentic-Law-Firm.git
cd Agentic-Law-Firm

# Install Python and MCP-server dependencies into a project venv (REQUIRED).
# Without this step every local MCP server will fail to launch.
bash scripts/install-mcp-deps.sh

# Activate the venv before starting the agent runtime
source .venv/bin/activate

# Smoke-test that every MCP server can start
bash scripts/test-mcp.sh

# Open the project in your agent runtime
agy            # Option A — Google Antigravity
# or
claude         # Option B — Claude Code

# In the agent shell, run the onboarding wizard
/onboard
```

The `/onboard` wizard walks you through jurisdictions (CN / SG / US / cross-border), practice areas, MCP install confirmation, statute library, hard-gate preferences, and identity. Total time: under five minutes.

先按第 2 节装好前置依赖，然后：

```bash
git clone https://github.com/huodebing-alt/Agentic-Law-Firm.git
cd Agentic-Law-Firm

# 把 Python 与 MCP server 依赖装到项目 venv（**必需**）。
# 不跑这一步，所有本地 MCP server 在启动时都会失败。
bash scripts/install-mcp-deps.sh

# 启动 agent runtime 前激活 venv
source .venv/bin/activate

# 冒烟测试：验证每个 MCP server 都能起来
bash scripts/test-mcp.sh

# 在 agent runtime 中打开本项目
agy            # 方案 A —— Google Antigravity
# 或
claude         # 方案 B —— Claude Code

# 在 agent shell 里运行引导向导
/onboard
```

`/onboard` 向导会带你过一遍：执业司法管辖区（CN/SG/US/跨境）、业务领域、MCP 安装确认、法规库、hard-gate 偏好、身份。全程不超过五分钟。

## 4. Features

- 100+ specialist agents across corporate, individual, contracts, compliance,
  IP, disputes, tax, labour, real estate, immigration, document-ops, research,
  drafting, onboarding.
- 150+ skills, each a self-contained workflow (contract review, M&A due
  diligence checklist, trademark filing prep, labour-arbitration response,
  individual immigration packet, ...).
- 27 MCP connectors stubbed and ready to wire: statutes-rag, wenshu, SAMR,
  CNIPA, pkulaw, wkinfo, chinalawinfo, Westlaw, LexisNexis, tianyancha,
  qichacha, fadada, e-sign, iManage, NetDocuments, M365, Gmail, GDrive,
  GCal, OneDrive, SharePoint, Box, Dropbox, Notion, Slack, Zoom, Teams.
- 20+ .docx templates, every one rendered per GB/T 9704—2012 plus law-firm
  convention (FangSong body, 28pt line spacing, A4 with 3.7/2.6/3.5/2.8cm
  margins, 2-character first-line indent, no emoji, no colour except a single
  dark-red warning style).
- Hard gates — any filing, any deal above your threshold, anything affecting
  a personal right, anything that names opposing counsel — pauses for human
  approval.
- Fresh-context decomposition for matters above ~15 sub-tasks.
- Onboarding wizard that installs only what you asked for.

100+ 专家 agent，涵盖公司、个人、合同、合规、知识产权、争议解决、税务、劳动、
不动产、移民、文档操作、研究、起草、引导上手共 14 个目录。
150+ skill，每一个都是一段自洽的工作流（合同审查、并购尽调清单、商标申请准备、
劳动仲裁应诉、个人移民材料包……）。
27 个 MCP 连接器已 stub 完成、可直接接真实接口：statutes-rag、裁判文书网、市场
监督总局、国家知识产权局、北大法宝、威科先行、北大法意、Westlaw、LexisNexis、
天眼查、企查查、法大大、e签宝、iManage、NetDocuments、M365、Gmail、GDrive、
GCal、OneDrive、SharePoint、Box、Dropbox、Notion、Slack、Zoom、Teams。
20+ docx 模板，全部按 GB/T 9704—2012 与律所惯例排版（仿宋_GB2312 正文、28 磅
固定行距、A4 上 3.7/右 2.6/下 3.5/左 2.8 厘米页边距、首行缩进 2 字符、无 emoji、
除单一深红色警示样式外无任何彩色）。
hard-gate 机制：任何政府申报、任何超过你设定阈值的合同、任何影响人身权利的文件、
任何在外发邮件中点名对方代理人的内容，都会暂停等你拍板。
任务规模超过约 15 个子任务时自动启用 fresh-context decomposition。
引导向导只会安装你勾选的部件。

## 4a. Supported Jurisdictions

| Jurisdiction | Primary law sources | MCP connectors | Specialist agents | Skills | Templates |
|---|---|---|---|---|---|
| China (CN) | 民法典 / 公司法 / 反垄断法 / 个人信息保护法 / 数据安全法 + 12 more, 17 total | 4 dedicated (statutes-rag, wenshu, samr, cnipa) + 23 cross-jurisdiction | 100+ | 152 | 20 |
| Singapore (SG) | Companies Act 1967, Employment Act, PDPA, SFA, Women's Charter, Trade Marks Act, Patents Act, Copyright Act 2021, Trustees Act, MCA + 6 more, 16 total | 8 (SSO, ACRA BizFile+, IPOS, IRAS, LawNet, MAS public, SLW, SICC/SIAC) | 10 | 33 | 10 |
| United States (US) | USC Titles 11/15/17/26/28/29/35/42, DGCL, CCPA/CPRA, NY BCL, Texas BOC, 12 items | 5 (Cornell LII, CourtListener, SEC EDGAR, USPTO, PACER stub) | 13 | 37 | 10 |
| Cross-border | Combined | All of the above | 4 | 10 | shared |

## 4a. 支持的司法管辖区

| 司法管辖区 | 主要法源 | MCP 连接器 | 专家 agent | skill | 模板 |
|---|---|---|---|---|---|
| 中国 (CN) | 民法典 / 公司法 / 反垄断法 / 个人信息保护法 / 数据安全法 等 17 部 | 专属 4 个（statutes-rag、裁判文书网、SAMR、CNIPA）+ 23 个跨法域 | 100+ | 152 | 20 |
| 新加坡 (SG) | Companies Act 1967、Employment Act、PDPA、SFA、Women's Charter、Trade Marks Act、Patents Act、Copyright Act 2021、Trustees Act、MCA 等 16 部 | 8 个（SSO、ACRA BizFile+、IPOS、IRAS、LawNet、MAS、SLW、SICC/SIAC） | 10 | 33 | 10 |
| 美国 (US) | USC Title 11/15/17/26/28/29/35/42、DGCL、CCPA/CPRA、NY BCL、Texas BOC，共 12 项 | 5 个（Cornell LII、CourtListener、SEC EDGAR、USPTO、PACER stub） | 13 | 37 | 10 |
| 跨境 | 以上合并 | 全部 | 4 | 10 | 共享 |

## 4b. Cross-Border Workflows

Typical multi-jurisdiction patterns the firm now handles end-to-end:
- CN tech company US IPO (VIE structure, CFIUS pre-screen, HFCAA compliance, SEC S-1/F-1)
- CN group establishing a SG regional holding (ODI / MOFCOM / SAFE outbound, ACRA incorporation, CN-SG DTAA)
- US fund acquiring CN target through SG SPV (HSR, CFIUS, MOFCOM filing, SG hub substance test)
- Cross-jurisdiction data programme (PIPL + PDPA + CCPA/CPRA harmonised privacy notice)
- Tri-jurisdiction dispute forum selection (CIETAC vs SIAC vs SICC vs US federal vs ICC)

## 4b. 跨境业务流程

典型多法域业务：
- 中国科技公司赴美上市（VIE 架构、CFIUS 预审、HFCAA 合规、SEC S-1 / F-1）
- 中国集团设立新加坡区域控股（ODI / MOFCOM / SAFE 境外投资、ACRA 注册、中新双边税收协定）
- 美元基金通过新加坡 SPV 收购中国标的（HSR、CFIUS、商务部、新加坡控股实质性测试）
- 跨法域数据合规项目（PIPL + PDPA + CCPA/CPRA 三法域统一隐私政策）
- 三法域争议管辖选择（CIETAC / SIAC / SICC / 美国联邦法院 / ICC 多选）

## 4c. Document Style by Jurisdiction

- **CN**: A4, 3.7/2.6/3.5/2.8cm margins, 方正小标宋 title / 黑体 H1 / 楷体_GB2312 H2 / 仿宋_GB2312 body, 28pt fixed line spacing, 2-character first-line indent, GB/T 7714-2015 citation.
- **SG**: A4, 25mm margins, Times New Roman 12pt body, 1.5 line spacing, 1.1.1 paragraph numbering, justify, SAL Style Guide (3rd ed.) citation.
- **US**: US Letter (8.5×11), 1 inch margins, Times New Roman 12pt body, double-spaced (1.5 for transactional), 0.5 inch first-line indent, left-align, Bluebook 21st citation, page number centred bottom (skip first).

Full per-jurisdiction spec: `docs/DOCUMENT_STYLE_GUIDE.md`.

## 4c. 各法域文书规范

- **中国 (CN)**：A4，3.7/2.6/3.5/2.8 厘米页边距，方正小标宋大标题、黑体一级、楷体_GB2312 二级、仿宋_GB2312 正文，28 磅固定行距，首行缩进 2 字符，引用按 GB/T 7714-2015。
- **新加坡 (SG)**：A4，25mm 页边距，Times New Roman 12pt 正文，1.5 倍行距，1.1.1 段落编号，两端对齐，引用按 SAL Style Guide 第 3 版。
- **美国 (US)**：US Letter（8.5×11 英寸），1 英寸页边距，Times New Roman 12pt 正文，双倍行距（交易文档 1.5 倍），首行缩进 0.5 英寸，左对齐，引用按 Bluebook 第 21 版，页码居中底部（首页不显示）。

详见 `docs/DOCUMENT_STYLE_GUIDE.md`。

## 5. Architecture

```
user ───────► task-router ─────────► specialist agents ─────► aggregator ─► user
                  │                       │      │
                  │                       │      └─► doc-ops (draft / redline / format)
                  │                       └─► research (statute / judgment / regulator)
                  ├─► task-decomposer (fresh context when scope > ~15 sub-tasks)
                  └─► hard-gate-keeper (human approval on the hard-gate list)
```

Single operator pattern: you talk to one agent (`task-router`), it dispatches,
the rest of the firm assembles in the background, and the partner reviewer
(`hard-gate-keeper`) refuses to ship anything sensitive without your sign-off.

单人指挥模式：你只跟 task-router 一个 agent 说话，它来派单，整间虚拟律所在后台
组装，hard-gate-keeper 这个「合伙人复核」角色在你点头之前不会放敏感内容出门。

## 6. Onboarding

`/onboard` collects five answers, then runs `scripts/onboard.py`:
1. Practice area: corporate / individual / both
2. MCP install: all / selected / none
3. Statute library: all 17 / selected / none
4. Hard gates: on / off (default on, with the default deal-value threshold)
5. Identity: solo / firm / in-house / learning

The script writes `.agentic-law-firm-config.json` and registers the MCPs you
asked for. You can re-run `/onboard` any time to reconfigure.

`/onboard` 只问五个问题，然后调 `scripts/onboard.py`：
1. 业务领域：公司 / 个人 / 两者
2. MCP 安装：全部 / 勾选 / 都不装
3. 法规库：全 17 部 / 勾选 / 都不下载
4. hard-gate：开 / 关（默认开，自带默认金额阈值）
5. 身份：单飞律师 / 律所 / 法务 / 学习者

脚本会把你的选择写进 `.agentic-law-firm-config.json`，并按你勾选的把 MCP 注册
上去。任何时候都可以重跑 `/onboard` 重配。

## 7. Tech Stack

Google Antigravity (`agy`), Claude Code (`claude`), Python 3.10+, python-docx
for .docx generation, FastMCP / mcp SDK for MCP servers. No build step, no
front-end, no database — everything is plain files on disk.

Statute sources: zh.wikisource.org / flk.npc.gov.cn (CN), sso.agc.gov.sg (SG), law.cornell.edu (US). Case-law sources: CourtListener / Free Law Project (US, free tier), LawNet (SG, subscription), 裁判文书网 (CN).

技术栈：Google Antigravity (`agy`)、Claude Code (`claude`)、Python 3.10+、
python-docx 负责生成 docx、FastMCP / mcp SDK 负责 MCP server。无需构建、无前端、
无数据库——所有内容都是磁盘上的纯文件。

法源：zh.wikisource.org / 国家法律法规数据库（CN）、sso.agc.gov.sg（SG）、law.cornell.edu（US）。判例：CourtListener / Free Law Project（US 免费档）、LawNet（SG 订阅）、裁判文书网（CN）。

## 8. Document Style

Black on white. No emoji. No decorative colour. The only allowed coloured
element in a deliverable is a dark-red (#8B0000) bold critical-warning block.
Typography follows GB/T 9704—2012: 方正小标宋简体 二号 title, 黑体 三号 H1,
楷体_GB2312 三号 H2, 仿宋_GB2312 三号 body, 28pt fixed line spacing, 2-character
first-line indent, A4 with 3.7/2.6/3.5/2.8cm margins. Times New Roman for
English and digits. Full spec: `docs/DOCUMENT_STYLE_GUIDE.md`.

黑字白底。无 emoji。无装饰彩色。交付物中唯一允许的有色元素是深红色（#8B0000）
加粗的「关键警示」段落。排版遵循 GB/T 9704—2012：方正小标宋简体二号大标题、
黑体三号一级标题、楷体_GB2312 三号二级标题、仿宋_GB2312 三号正文、28 磅固定
行距、首行缩进 2 字符、A4 上 3.7 右 2.6 下 3.5 左 2.8 厘米页边距、英文数字
Times New Roman。完整规范见 `docs/DOCUMENT_STYLE_GUIDE.md`。

## 9. Roadmap

- v0.1 (this release): full agent / skill / MCP scaffolding with stub MCPs,
  document templates, onboarding, hard gates.
- v0.2: wire real backends for statutes-rag (PKULaw / 国家法律法规数据库),
  wenshu, CNIPA, SAMR.
- v0.3: bilingual deliverable templates (CN/EN side-by-side memos and SPAs).
- v0.4: arbitration-rule packs (CIETAC, HKIAC, SIAC, ICC) + tribunal-side
  procedural assistants.
- v0.5: knowledge-management integration (iManage / NetDocuments / Notion
  search routed through doc-ops).

v0.1（本版本）：agent / skill / MCP 完整骨架 + stub MCP + 文书模板 + 引导向导 +
hard-gate。
v0.2：把 statutes-rag（北大法宝 / 国家法律法规数据库）、裁判文书网、CNIPA、
市场监督总局接到真实数据。
v0.3：中英对照交付物模板（CN/EN 对照备忘录与 SPA）。
v0.4：仲裁规则包（CIETAC、HKIAC、SIAC、ICC）+ 庭审程序辅助 agent。
v0.5：知识管理集成（iManage / NetDocuments / Notion 检索通过 doc-ops 调度）。

## 10. Disclaimer

Outputs of this project are drafts and research aids only. They do not
constitute legal advice and do not create an attorney-client relationship.
Do not file, submit, sign, or rely on any output without independent review
by a qualified attorney in the relevant jurisdiction. See `DISCLAIMER.md`.

本项目的任何输出仅为草稿与研究辅助，**不构成法律意见**，也**不形成委托代理
关系**。未经在相关司法辖区有执业资格的律师独立复核，请勿提交、递交、签署或据
以行事。详见 `DISCLAIMER.md`。

## 11. License

MIT. See `LICENSE`.
MIT 许可。详见 `LICENSE`。

## 12. Acknowledgments

Thanks to Anthropic (Claude Code), Google (Antigravity), and the open MCP
ecosystem. Particular thanks to the maintainers of the Chinese-law open
data sources whose efforts make tools like this possible.

致谢 Anthropic（Claude Code）、Google（Antigravity）以及整个开放 MCP 生态。
特别致谢维护中国法律开放数据源的同行——没有他们的工作，这类工具不可能存在。

## 13. Sponsor

Agentic-Law-Firm is free and open source. If it saves you time or helps you close your matter, consider supporting continued development:

- [Buy Me a Coffee](https://buymeacoffee.com/bieng) — one-time support
- [GitHub Sponsors](https://github.com/sponsors/huodebing-alt) — recurring support through GitHub

Sponsorships help fund time spent maintaining skills, adding new agents, keeping up with Antigravity, Claude Code and engine API changes, and responding to community issues.

Agentic-Law-Firm 是免费开源项目。如果它替你省下时间、帮你把案子推进，欢迎支持后续开发：

- [Buy Me a Coffee](https://buymeacoffee.com/bieng) —— 一次性请杯咖啡
- [GitHub Sponsors](https://github.com/sponsors/huodebing-alt) —— 通过 GitHub 持续赞助

你的赞助会用于维护 skill、新增 agent、跟进 Antigravity 与 Claude Code 的接口变更，以及回应社区问题。
