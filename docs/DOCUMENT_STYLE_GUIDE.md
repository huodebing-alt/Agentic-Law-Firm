# Document Style Guide

The single source of truth for Agentic-Law-Firm deliverables.
All `.docx` outputs must satisfy this guide. The machine-readable
spec is `templates/_style/style-config.json`; the print-CSS version
is `templates/_style/lawfirm-style.css`.

## Why this exists

A lawyer reading our output should not be able to tell whether the
draft was produced by an associate or by an agent. Document style
is the most visible signal of professionalism. We follow GB/T
9704—2012 (the PRC government-document standard) plus the
established Chinese law-firm convention for litigation and
transactional papers.

## Page

- Size: A4
- Margins: 3.7 cm top / 2.6 cm right / 3.5 cm bottom / 2.8 cm left
- 22 lines per page, 28 characters per line (target)

## Fonts (Chinese)

| Role | Font | Size |
|------|------|------|
| Title (大标题) | 方正小标宋简体 (fallback: 宋体) | 22 pt (二号) |
| H1 (一、) | 黑体 | 16 pt (三号) bold |
| H2 ((一)) | 楷体_GB2312 | 16 pt (三号) |
| H3 (1.) | 仿宋_GB2312 bold | 16 pt (三号) |
| Body | 仿宋_GB2312 | 16 pt (三号) |
| Statute quote | 仿宋_GB2312 | 14 pt (小三) |
| Signature block | 楷体_GB2312 | 16 pt (三号) |
| Footer / page no. | 仿宋_GB2312 | 10.5 pt (五号) |

Civil and commercial pleadings may use 宋体 12 pt body at 1.5
line spacing where local court rules require it; default remains
above.

## Fonts (English and digits)

Times New Roman everywhere English text or digits appear inline.
Do not let Chinese fonts render English — the spacing breaks.

## Paragraph rules

- Line spacing: 28 pt fixed (公文标准). Civil-pleading variant: 1.5
  lines.
- First-line indent: 2 characters (`2em`).
- Alignment: justified (`两端对齐`).
- Inter-paragraph spacing: 0.

## Headings

Use Chinese ordinals exactly:
- H1: `一、`, `二、`, `三、` ...
- H2: `（一）`, `（二）`, `（三）` ...
- H3: `1.`, `2.`, `3.` ...
- H4: `（1）`, `（2）`, `（3）` ...
- H5: `①`, `②`, `③` ...

## Statute and case citations

Statute: `《民法典》第五百零九条`. Always include statute name and
article number in Chinese. For sub-clauses, use `第X条第Y款第Z项`.

Case: `(2024)京01民终xxxx号` — court code + case-type code + serial,
followed by court name. For Supreme People's Court guiding cases,
add `(指导案例第XXX号)`.

## Critical warnings

The only coloured element permitted in a deliverable is the
`critical-warning` block:

- Text colour: `#8B0000` (dark red)
- Bold
- Border: 1.5 pt solid black
- Padding: 0.5 em vertical / 1 em horizontal
- No first-line indent

Use sparingly. One per memo at most. Reserve for material-risk
warnings that the partner-in-charge needs to act on.

## Forbidden

- Emoji of any kind, anywhere.
- Background colour or background image.
- Decorative coloured text (other than the dark-red critical
  warning).
- Banner, ASCII art, decorative dividers.
- Marketing voice (no "delightful", "stunning", "next-generation").




## 4. Singapore style

- **Page**: A4, 25mm margins on all sides.
- **Body font**: Times New Roman 12pt.
- **Headings**: Times New Roman, 12pt bold (sometimes 14pt for title).
- **Line spacing**: 1.5 (some firms use single in tables).
- **Paragraph numbering**: hierarchical `1.`, `1.1`, `1.1.1`.
- **Alignment**: justify.
- **First-line indent**: none (block paragraphs).
- **Citation**: SAL Style Guide (3rd ed., 2021). Statutes by short title
  and section, case names italicised, neutral citations preferred.
- **Colour**: black on white. Single dark-red (#8B0000) for critical-warning
  blocks only.
- **Page numbers**: right footer.

## 4. 新加坡格式（中文版）

- 纸张 A4，四边 25mm 页边距
- 正文 Times New Roman 12 号
- 标题 Times New Roman 12 号粗体（封面标题可 14 号）
- 行距 1.5 倍（表格内可单倍）
- 段落编号采用 1. / 1.1 / 1.1.1 层级
- 两端对齐
- 不缩进首行（块段落）
- 引用：SAL Style Guide 第 3 版（2021）；制定法用 short title + 条款；案例名斜体；优先使用中性引文
- 颜色：黑字白底，仅允许深红 #8B0000 用于关键警示段
- 页码：右页脚

## 5. United States style

- **Page**: US Letter (8.5 × 11 in), 1 inch margins on all sides.
- **Body font**: Times New Roman 12pt (some courts allow 14pt for elderly).
- **Headings**: Times New Roman, 12-14pt bold.
- **Line spacing**: 2.0 (court filings, briefs); 1.5 acceptable for
  transactional. Block quotes single-spaced, indented.
- **Paragraph indent**: 0.5 inch first-line.
- **Alignment**: left-align (court filings typically); justify acceptable for
  transactional.
- **Citation**: The Bluebook (Columbia / Harvard / Penn / Yale Law Review
  Association, 21st ed.). Cases italicised in text, signal usage per Rule
  1.2, jump citations required.
- **Colour**: black on white. Single dark-red (#8B0000) for critical-warning
  blocks only.
- **Page numbers**: centred bottom, skip first page.

## 5. 美国格式（中文版）

- 纸张 US Letter（8.5 × 11 英寸），四边 1 英寸页边距
- 正文 Times New Roman 12 号（少数法院允许 14 号供长者阅读）
- 标题 Times New Roman 12-14 号粗体
- 行距 2.0（诉讼文书 / 出庭文件）；交易文件可 1.5；引用段单倍并缩进
- 段落首行缩进 0.5 英寸
- 左对齐（诉讼）；交易文件可两端对齐
- 引用：Bluebook 第 21 版；正文中案例名斜体；signal 使用按 Rule 1.2；必须 jump cite
- 颜色：黑字白底，仅允许深红 #8B0000 用于关键警示段
- 页码：居中底部，封面不显示

## 6. Cross-jurisdiction documents

When a deliverable spans multiple jurisdictions (e.g. a memo discussing
PDPA + CCPA + PIPL together), pick the document style of the governing
jurisdiction for the contract; if the memo is advisory only, pick the
style of the firm's home base, and use the other jurisdictions' citation
formats within the body.

跨法域文件：合同按管辖法的格式；纯咨询备忘录按律所所在地的格式，引用其他
法域时各用各自的引文规范。
