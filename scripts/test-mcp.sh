#!/usr/bin/env bash
# test-mcp.sh <name>  — simple sanity check that the named MCP stub server
# imports cleanly. Real round-trip tests require an MCP client.

set -euo pipefail
name="${1:?usage: test-mcp.sh <server-name>}"
cd "$(dirname "$0")/.."

if [[ ! -f "mcp-servers/${name}/server.py" ]]; then
  echo "no such server: ${name}"
  exit 1
fi
python3 -c "import importlib.util, sys; \
             spec = importlib.util.spec_from_file_location('s', 'mcp-servers/${name}/server.py'); \
             m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); \
             print('[test-mcp] ${name} imports OK')"
