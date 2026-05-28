"""MCP stub server: CNIPA (国家知识产权局).

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
        "server": "cnipa",
        "args": args,
        "result": {"results": [{"app_no": "[STUB] 12345678", "mark": "示例商标", "class": "9", "status": "已注册", "owner": "示例公司"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("cnipa")

    @mcp.tool()
    def cnipa_search(keyword: str = "", type: str = "", class: str = "", limit: str = "") -> dict:
        """Search the CNIPA database for trademarks and patents. Returns application number, status, owner, dates."""
        return _stub_response({"keyword": keyword, "type": type, "class": class, "limit": limit})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
