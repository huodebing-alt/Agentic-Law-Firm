"""MCP stub server: NetDocuments.

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
        "server": "netdocuments-stub",
        "args": args,
        "result": {"results": [{"doc_id": "[STUB] ABC123", "title": "Sample NetDocs doc"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("netdocuments-stub")

    @mcp.tool()
    def netdocs_search(query: str = "") -> dict:
        """Search NetDocuments for documents and matters."""
        return _stub_response({"query": query})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
