"""MCP stub server: China Judgment Documents (裁判文书网).

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
        "server": "wenshu",
        "args": args,
        "result": {"results": [{"title": "[STUB] 关于合同诈骗的判决摘要", "court": "最高人民法院", "date": "2024-03-01", "case_no": "(2024)最高法民终xxx号", "url": "https://wenshu.court.gov.cn/website/wenshu/..."}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("wenshu")

    @mcp.tool()
    def search_judgments(keyword: str = "", court: str = "", year: str = "", limit: str = "") -> dict:
        """Search PRC court judgments by keyword. Returns title, court, date, case number, URL."""
        return _stub_response({"keyword": keyword, "court": court, "year": year, "limit": limit})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
