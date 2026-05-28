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
