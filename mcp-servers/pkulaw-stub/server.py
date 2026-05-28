"""MCP stub server: PKULaw (北大法宝).

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
        "server": "pkulaw-stub",
        "args": args,
        "result": {"results": [{"title": "[STUB] 中华人民共和国数据安全法", "category": "law", "url": "https://www.pkulaw.com/..."}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("pkulaw-stub")

    @mcp.tool()
    def pkulaw_search(query: str = "", category: str = "", limit: str = "") -> dict:
        """Search PKULaw for statutes, cases, and articles. Returns title and a snippet."""
        return _stub_response({"query": query, "category": category, "limit": limit})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
