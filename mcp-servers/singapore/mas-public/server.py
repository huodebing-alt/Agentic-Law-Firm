"""MCP stub server: sg-mas-public.

Monetary Authority of Singapore public data (mas.gov.sg). Notices, guidelines, FI register.

STATUS: stub. Returns mock data so the agent harness loads cleanly.
To wire real backend, replace the body of the tool functions below.
See README.md alongside this server for the real-API target.
"""
from __future__ import annotations

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    FastMCP = None  # type: ignore


def _stub_response(args: dict) -> dict:
    return {
        "status": "stub",
        "server": "sg-mas-public",
        "args": args,
        "result": {"hits": [{"notice": "[STUB] MAS Notice 626", "topic": "AML/CFT", "url": "https://www.mas.gov.sg/..."}]},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("sg-mas-public")

    @mcp.tool()
    def search_notices(query: str = "") -> dict:
        """Search MAS Notices and Guidelines."""
        return _stub_response({"query": query})

    @mcp.tool()
    def get_fi_register(entity: str = "") -> dict:
        """Check the MAS FI register."""
        return _stub_response({"entity": entity})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
