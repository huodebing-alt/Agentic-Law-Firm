# Agentic-Law-Firm

> A single operator commanding a virtual law firm.
> 一个人，指挥一整间虚拟律所。

100+ specialist agents, 150+ workflow skills, 27 MCP connectors, 20+ document
templates. Built primarily for Google Antigravity; also runs on Claude Code.
Chinese law (primary) and general / cross-border matters (secondary).

100+ 专家 agent、150+ 工作 skill、27 个 MCP 连接器、20+ 文书模板。主要面向
Google Antigravity，同时兼容 Claude Code。以中国法为主、通用法 / 跨境业务为辅。

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

## 2. Quickstart

```bash
git clone https://github.com/huodebing-alt/Agentic-Law-Firm.git
cd Agentic-Law-Firm
pip install -r requirements.txt

# Option A — Google Antigravity
agy            # opens the project; then type /onboard

# Option B — Claude Code
claude         # opens the project; then type /onboard
```

The `/onboard` wizard walks you through practice areas, MCP install, statute
library, hard-gate preferences, and identity. Total time: under five minutes.

```bash
git clone https://github.com/huodebing-alt/Agentic-Law-Firm.git
cd Agentic-Law-Firm
pip install -r requirements.txt

# 方案 A —— Google Antigravity
agy            # 打开项目，然后输入 /onboard

# 方案 B —— Claude Code
claude         # 打开项目，然后输入 /onboard
```

`/onboard` 向导会带你过一遍：业务领域、MCP 安装、法规库、hard-gate 偏好、身份。
全程不超过五分钟。

## 3. Features

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

## 4. Architecture

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

## 5. Onboarding

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

## 6. Tech Stack

Google Antigravity (`agy`), Claude Code (`claude`), Python 3.10+, python-docx
for .docx generation, FastMCP / mcp SDK for MCP servers. No build step, no
front-end, no database — everything is plain files on disk.

技术栈：Google Antigravity (`agy`)、Claude Code (`claude`)、Python 3.10+、
python-docx 负责生成 docx、FastMCP / mcp SDK 负责 MCP server。无需构建、无前端、
无数据库——所有内容都是磁盘上的纯文件。

## 7. Document Style

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

## 8. Roadmap

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

## 9. Disclaimer

Outputs of this project are drafts and research aids only. They do not
constitute legal advice and do not create an attorney-client relationship.
Do not file, submit, sign, or rely on any output without independent review
by a qualified attorney in the relevant jurisdiction. See `DISCLAIMER.md`.

本项目的任何输出仅为草稿与研究辅助，**不构成法律意见**，也**不形成委托代理
关系**。未经在相关司法辖区有执业资格的律师独立复核，请勿提交、递交、签署或据
以行事。详见 `DISCLAIMER.md`。

## 10. License

MIT. See `LICENSE`.
MIT 许可。详见 `LICENSE`。

## 11. Acknowledgments

Thanks to Anthropic (Claude Code), Google (Antigravity), and the open MCP
ecosystem. Particular thanks to the maintainers of the Chinese-law open
data sources whose efforts make tools like this possible.

致谢 Anthropic（Claude Code）、Google（Antigravity）以及整个开放 MCP 生态。
特别致谢维护中国法律开放数据源的同行——没有他们的工作，这类工具不可能存在。

## 12. Sponsor

If Agentic-Law-Firm saved your firm even one billable hour this week — the
kind you'd rather have spent on judgment than on formatting — that hour is
worth more than the coffee. [Buy me that coffee](https://github.com/sponsors/huodebing-alt).

I built this so lawyers can spend their hours where their training actually
matters. If it works for you, your support keeps it improving.

[大佬要打赏杯咖啡钱吗？](https://github.com/sponsors/huodebing-alt)

> Note: if the link 404s, the sponsor profile has not been published yet.
> Enable it at GitHub Settings → Sponsors → Set up your profile, and the
> same URL will start working.
>
> 备注：如果链接 404，说明 Sponsor profile 还没启用。到 GitHub Settings
> → Sponsors → Set up your profile 启用即可，同一个链接会自动生效。
