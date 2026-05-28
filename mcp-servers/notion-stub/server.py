"""MCP stub server: Notion.

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
        "server": "notion-stub",
        "args": args,
        "result": {"results": [{"id": "[STUB] notion-page-id", "title": "Sample matter page"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("notion-stub")

    @mcp.tool()
    def notion_call(action: str = "", query: str = "") -> dict:
        """Call a Notion API endpoint (search, retrieve page, append block)."""
        return _stub_response({"action": action, "query": query})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
