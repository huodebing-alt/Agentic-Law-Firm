"""MCP stub server: us-courtlistener.

CourtListener / Free Law Project (courtlistener.com). US case law search and PACER docket integration.

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
        "server": "us-courtlistener",
        "args": args,
        "result": {"hits": [{"citation": "[STUB] 555 U.S. 1 (2008)", "case": "Example v. Example", "court": "U.S.", "snippet": "..."}]},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("us-courtlistener")

    @mcp.tool()
    def search(q: str = "", court: str = "") -> dict:
        """Search US case law and docket entries."""
        return _stub_response({"q": q, "court": court})

    @mcp.tool()
    def get_case(id_or_citation: str = "") -> dict:
        """Get a case by id or citation."""
        return _stub_response({"id_or_citation": id_or_citation})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
