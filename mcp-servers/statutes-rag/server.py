"""MCP stub server: Statutes RAG.

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
        "server": "statutes-rag",
        "args": args,
        "result": {"results": [{"citation": "《民法典》第五百零九条", "title": "合同的履行原则", "effective": "2021-01-01", "article_text": "[STUB] 当事人应当按照约定全面履行自己的义务。"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("statutes-rag")

    @mcp.tool()
    def lookup_statute(query: str = "", limit: str = "") -> dict:
        """Look up a PRC statute / regulation / judicial interpretation by topic or citation. Returns citation, effective date, and article text."""
        return _stub_response({"query": query, "limit": limit})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
