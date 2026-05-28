"""MCP stub server: SAMR (国家市场监督管理总局).

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
        "server": "samr",
        "args": args,
        "result": {"results": [{"title": "[STUB] 关于某经营者集中的反垄断决定", "date": "2024-04-01", "url": "https://www.samr.gov.cn/..."}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("samr")

    @mcp.tool()
    def samr_lookup(keyword: str = "", year: str = "", limit: str = "") -> dict:
        """Look up SAMR enforcement actions, antitrust decisions, fair-competition reviews, advertising decisions."""
        return _stub_response({"keyword": keyword, "year": year, "limit": limit})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
