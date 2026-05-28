# statutes/

Holds local copies of PRC statutes downloaded by
`scripts/prepare-statutes.py`. The manifest in `manifest.json` lists
the 17 core statutes used by `statutes-rag` and the various
specialists.

Files are downloaded into `statutes/data/<key>.md` on first
onboarding (or by manual re-run of the script). The v0.1 release
writes placeholder files only; real text fetching is a v0.2 task.
