# Jurisdiction Guide

Three-jurisdiction comparison and decision tree for when to invoke which
specialist. Bilingual (EN / CN).

## 1. Quick comparison

| Topic | China (CN) | Singapore (SG) | United States (US) |
|---|---|---|---|
| Legal tradition | Civil law / statutory | Common law (English heritage, statutory overlay) | Common law (federal + state) |
| Primary corporate vehicle | 有限责任公司 / 股份有限公司 | Private company limited by shares (Pte Ltd) | Delaware C-corp, LLC, or state corp |
| Securities regulator | CSRC | MAS | SEC |
| Antitrust regulator | SAMR | CCCS | DOJ Antitrust + FTC |
| IP office | CNIPA | IPOS | USPTO |
| Privacy law | PIPL, Data Security Law, CSL | PDPA 2012 | CCPA/CPRA + 12 state laws + sectoral (HIPAA, GLBA) |
| Employment baseline | 劳动合同法 | Employment Act | FLSA / state |
| Family law | 民法典婚姻家庭编 | Women's Charter | State family code |
| Estate / probate | 民法典继承编 | Probate & Administration Act | State probate code |
| Citation style | GB/T 7714-2015 | SAL Style Guide (3rd ed.) | Bluebook 21st |

## 2. Decision tree

```
intake → task-router → jurisdiction-detector
                       │
        ┌──────────────┼─────────────┬──────────────┐
        │              │             │              │
       CN             SG            US         cross-border
        │              │             │              │
        ▼              ▼             ▼              ▼
   .claude/agents/  sg-*       us-*         cn-sg / cn-us /
   <area>/         specialists specialists  sg-us / tri-*
```

## 3. Common scenarios

- **CN tech company wants US IPO** → `cn-us-cross-border` + `us-securities-counsel` + `cn-us-vie-structure-readiness` + `cn-us-ipo-prep`.
- **US fund acquires CN target through SG SPV** → `cn-us-cross-border` + `cn-sg-cross-border` + `us-antitrust-counsel` (HSR) + `sg-corporate-counsel` + corresponding CN team.
- **Cross-jurisdiction privacy policy** → `compliance` (CN) + `sg-pdpa-specialist` + `us-privacy-counsel`.
- **CN employee transferring to SG office** → `labor` (CN) + `sg-employment-specialist` + `sg-mom-work-pass-strategy`.

## 1. 速览对比

| 主题 | 中国 (CN) | 新加坡 (SG) | 美国 (US) |
|---|---|---|---|
| 法系 | 大陆法 / 制定法 | 普通法（英国传统 + 制定法补强） | 普通法（联邦 + 各州） |
| 主要公司形态 | 有限责任公司 / 股份有限公司 | Pte Ltd（私人股份有限公司） | 特拉华 C-corp / LLC / 各州公司 |
| 证券监管 | 证监会 | MAS | SEC |
| 反垄断监管 | 国家市场监督管理总局 | CCCS | 司法部反垄断局 + FTC |
| IP 局 | 国家知识产权局 | IPOS | USPTO |
| 隐私法 | 个人信息保护法 / 数据安全法 / 网络安全法 | PDPA 2012 | CCPA/CPRA + 12 部州法 + 行业法（HIPAA / GLBA） |
| 劳动基线 | 劳动合同法 | Employment Act | FLSA / 各州 |
| 家事法 | 民法典婚姻家庭编 | Women's Charter | 各州家事法典 |
| 遗产 / 遗嘱 | 民法典继承编 | Probate & Administration Act | 各州遗嘱认证法典 |
| 引用规范 | GB/T 7714-2015 | SAL Style Guide 第 3 版 | Bluebook 第 21 版 |

## 2. 决策树（中文版）

接案 → task-router → jurisdiction-detector → CN/SG/US/跨境 → 对应专家

## 3. 典型场景

- **中国科技公司赴美 IPO**：`cn-us-cross-border` + `us-securities-counsel` + `cn-us-vie-structure-readiness` + `cn-us-ipo-prep`
- **美元基金借道新加坡 SPV 收购中国标的**：`cn-us-cross-border` + `cn-sg-cross-border` + `us-antitrust-counsel`（HSR）+ `sg-corporate-counsel` + 对应中方团队
- **跨法域隐私政策**：`compliance`（CN）+ `sg-pdpa-specialist` + `us-privacy-counsel`
- **中国员工调任新加坡办公室**：`labor`（CN）+ `sg-employment-specialist` + `sg-mom-work-pass-strategy`
