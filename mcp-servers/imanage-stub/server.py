"""MCP stub server: iManage.

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
        "server": "imanage-stub",
        "args": args,
        "result": {"results": [{"doc_id": "[STUB] 12345", "title": "Sample iManage doc"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("imanage-stub")

    @mcp.tool()
    def imanage_search(query: str = "", library: str = "") -> dict:
        """Search iManage document management for documents and matters."""
        return _stub_response({"query": query, "library": library})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
