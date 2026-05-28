# `_style/` — Document style assets

This directory holds the single source of truth for Agentic-Law-Firm
document formatting:

- `lawfirm-style.css` — HTML / print-CSS implementation. Use this when
  a deliverable is going out as HTML or being rendered to PDF via a
  headless browser.
- `style-config.json` — machine-readable spec read by
  `scripts/generate-templates.py` to produce all `.docx` templates,
  and by `doc-ops-formatter` to apply final formatting.

The style follows GB/T 9704—2012 plus Chinese law-firm convention:
A4 / 3.7-2.6-3.5-2.8 cm margins / 28-pt fixed line spacing /
2-character first-line indent / FangSong body, Hei H1, Kai H2,
FangSong H3, FangSong body, FZXiaoBiaoSong title. English and digits
use Times New Roman. Black text on white background; the only
coloured element permitted is the dark-red (`#8B0000`) bold
`critical-warning` block, used sparingly.

No emoji is ever used in client-facing deliverables.
