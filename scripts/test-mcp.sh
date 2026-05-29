#!/usr/bin/env bash
# test-mcp.sh — smoke-test every MCP server in this repo by importing its
# server.py. Catches missing-dependency failures BEFORE you start claude/agy
# and wonder why every connector is grey.
#
# Usage:
#   bash scripts/test-mcp.sh            # test all servers
#   bash scripts/test-mcp.sh <name>     # test a single server by directory name

set -uo pipefail
cd "$(dirname "$0")/.."

# If a venv exists prefer it (so we test against the deps actually installed).
if [ -d ".venv" ] && [ -z "${VIRTUAL_ENV:-}" ]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

PY=python3

run_one() {
  local path="$1"
  local name
  name=$(echo "$path" | sed 's#^mcp-servers/##; s#/server.py$##')
  local out
  if out=$($PY -c "
import importlib.util, sys, traceback
spec = importlib.util.spec_from_file_location('s', '$path')
m = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(m)
    print('OK')
except Exception:
    traceback.print_exc()
    sys.exit(1)
" 2>&1); then
    printf '  [PASS] %s\n' "$name"
    return 0
  else
    printf '  [FAIL] %s\n' "$name"
    printf '%s\n' "$out" | sed 's/^/         /'
    return 1
  fi
}

if [ $# -ge 1 ]; then
  TARGET="mcp-servers/$1/server.py"
  if [ ! -f "$TARGET" ]; then
    echo "no such server: $1"
    exit 1
  fi
  run_one "$TARGET"
  exit $?
fi

echo "[test-mcp] Importing every MCP server ..."
total=0
fail=0
for path in mcp-servers/*/server.py mcp-servers/*/*/server.py; do
  [ -f "$path" ] || continue
  total=$((total+1))
  if ! run_one "$path"; then
    fail=$((fail+1))
  fi
done

echo ""
echo "[test-mcp] $((total-fail))/$total servers OK, $fail failed."
if [ "$fail" -gt 0 ]; then
  echo "[test-mcp] Re-run 'bash scripts/install-mcp-deps.sh' to install missing deps."
  echo "[test-mcp] If a single server still fails, look at the traceback above and"
  echo "[test-mcp] check that server's own README for any extra steps (API key etc)."
  exit 1
fi
