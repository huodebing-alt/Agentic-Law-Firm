"""MCP stub server: ChinaLawInfo (北大法意).

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
        "server": "chinalawinfo-stub",
        "args": args,
        "result": {"results": [{"title": "[STUB] 公司法相关检索结果"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("chinalawinfo-stub")

    @mcp.tool()
    def chinalawinfo_search(query: str = "", limit: str = "") -> dict:
        """Search ChinaLawInfo for statutes and cases. Returns title and snippet."""
        return _stub_response({"query": query, "limit": limit})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
