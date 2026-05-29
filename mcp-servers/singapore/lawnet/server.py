"""MCP stub server: sg-lawnet.

LawNet (lawnet.sg) — subscription. SG case law and Singapore Law Reports.

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
        "server": "sg-lawnet",
        "args": args,
        "result": {"note": "Subscription required.", "hits": []},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("sg-lawnet")

    @mcp.tool()
    def search_cases(query: str = "", court: str = "") -> dict:
        """Search SG case law via LawNet (subscription required)."""
        return _stub_response({"query": query, "court": court})

    @mcp.tool()
    def get_case(citation: str = "") -> dict:
        """Retrieve a case by neutral citation."""
        return _stub_response({"citation": citation})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
