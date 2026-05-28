"""MCP stub server: Westlaw.

STATUS: stub. Returns mock data so the agent harness loads cleanly.
To wire real backend, replace the body of the tool functions below.
"""
from __future__ import annotations

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:  # graceful fallback if mcp SDK is not installed
    FastMCP = None  # type: ignore


def _stub_response(args: dict) -> dict:
    return {
        "status": "stub",
        "server": "westlaw-stub",
        "args": args,
        "result": {"results": [{"title": "[STUB] Sample Delaware Chancery decision", "citation": "[STUB] 2024 Del. Ch. ..."}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("westlaw-stub")

    @mcp.tool()
    def westlaw_search(query: str = "", jurisdiction: str = "", limit: str = "") -> dict:
        """Search Westlaw for US / UK / international cases and statutes."""
        return _stub_response({"query": query, "jurisdiction": jurisdiction, "limit": limit})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
