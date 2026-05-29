"""MCP stub server: us-pacer-stub.

PACER (pacer.uscourts.gov) — subscription. Federal court dockets and documents.

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
        "server": "us-pacer-stub",
        "args": args,
        "result": {"note": "Subscription required.", "hits": []},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("us-pacer-stub")

    @mcp.tool()
    def search_dockets(query: str = "", court: str = "") -> dict:
        """Search PACER federal-court dockets (subscription)."""
        return _stub_response({"query": query, "court": court})

    @mcp.tool()
    def get_docket(court: str = "", case_no: str = "") -> dict:
        """Get a docket by case number."""
        return _stub_response({"court": court, "case_no": case_no})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
