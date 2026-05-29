#!/usr/bin/env bash
# install-mcp-deps.sh — set up the project venv and install every dependency
# needed for the local MCP servers to launch.
#
# This script is idempotent. Re-run it any time the requirements change.
#
# After it finishes:
#   source .venv/bin/activate
#   bash scripts/test-mcp.sh
#   claude    # or:  agy

set -euo pipefail

cd "$(dirname "$0")/.."
ROOT="$(pwd)"

# 1. Check Python
if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 not found. Install Python 3.10+ first (see README section 2 Prerequisites)."
  exit 1
fi
PYV=$(python3 -c 'import sys;print("%d.%d"%sys.version_info[:2])')
PYMAJOR=$(python3 -c 'import sys;print(sys.version_info[0])')
PYMINOR=$(python3 -c 'import sys;print(sys.version_info[1])')
if [ "$PYMAJOR" -lt 3 ] || { [ "$PYMAJOR" -eq 3 ] && [ "$PYMINOR" -lt 10 ]; }; then
  echo "ERROR: Python $PYV found, but Agentic-Law-Firm needs >= 3.10."
  exit 1
fi
echo "[install-mcp-deps] Python $PYV detected."

# 2. Create venv if missing
if [ ! -d ".venv" ]; then
  echo "[install-mcp-deps] Creating .venv ..."
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

# 3. Upgrade pip
python3 -m pip install --upgrade pip >/dev/null

# 4. Install root requirements
if [ -f "requirements.txt" ]; then
  echo "[install-mcp-deps] Installing requirements.txt ..."
  pip install -r requirements.txt
fi

# 5. Install MCP shared requirements
if [ -f "mcp-servers/requirements.txt" ]; then
  echo "[install-mcp-deps] Installing mcp-servers/requirements.txt ..."
  pip install -r mcp-servers/requirements.txt
fi

# 6. Walk every mcp-servers/*/requirements.txt
for req in mcp-servers/*/requirements.txt mcp-servers/*/*/requirements.txt; do
  if [ -f "$req" ]; then
    echo "[install-mcp-deps] Installing $req ..."
    pip install -r "$req"
  fi
done

echo ""
echo "[install-mcp-deps] Done."
echo "Activate the venv with:   source .venv/bin/activate"
echo "Verify MCP servers:       bash scripts/test-mcp.sh"
echo "Then start the runtime:   claude   (or:  agy)"
