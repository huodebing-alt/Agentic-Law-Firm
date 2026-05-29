#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="Agentic-Law-Firm"
OWNER="huodebing-alt"
DESC="A single operator commanding a virtual law firm — 140+ agents, 230+ skills, 40 MCPs across CN/SG/US, runs on Google Antigravity and Claude Code."

if ! command -v gh >/dev/null 2>&1; then
  echo "Need GitHub CLI: https://cli.github.com/"
  exit 1
fi

gh auth status >/dev/null 2>&1 || { echo "Run: gh auth login"; exit 1; }

git init -q
git add .
git commit -q -m "Initial commit: Agentic-Law-Firm v0.2 (CN+SG+US)"
git branch -M main

gh repo create "${OWNER}/${REPO_NAME}" --public --description "${DESC}" --source=. --remote=origin --push

TOPICS=(
  "agentic-ai"
  "law-firm"
  "legal-tech"
  "chinese-law"
  "singapore-law"
  "us-law"
  "delaware-law"
  "pdpa"
  "ccpa"
  "cross-border-legal"
  "bluebook"
  "sal-style-guide"
  "multi-agent"
  "task-decomposition"
  "mcp"
  "antigravity"
  "claude-code"
  "model-agnostic"
  "legal-research"
  "contract-drafting"
  "doc-ops"
  "redline"
  "legal-ops"
)
for t in "${TOPICS[@]}"; do
  gh repo edit "${OWNER}/${REPO_NAME}" --add-topic "$t" || true
done

echo "Pushed: https://github.com/${OWNER}/${REPO_NAME}"
