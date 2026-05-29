"""MCP stub server: sg-singapore-law-watch.

Singapore Law Watch (singaporelawwatch.sg). Daily SG legal news headlines.

STATUS: stub. Returns mock data so the agent harness loads cleanly.
To wire real backend, replace the body of the tool functions below.
See README.md alongside this server for the real-API target.
"""
from __future__ import annotations

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    FastMCP = None  # type: ignore


def _stub_response(args: dict) -> dict:
    return {
        "status": "stub",
        "server": "sg-singapore-law-watch",
        "args": args,
        "result": {"items": [{"title": "[STUB] Court of Appeal clarifies fiduciary duty test", "url": "https://www.singaporelawwatch.sg/...", "date": "2026-05-29"}]},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("sg-singapore-law-watch")

    @mcp.tool()
    def list_headlines(date_from: str = "", date_to: str = "") -> dict:
        """List recent SG law news headlines."""
        return _stub_response({"date_from": date_from, "date_to": date_to})

    @mcp.tool()
    def get_article(url: str = "") -> dict:
        """Get a Singapore Law Watch article."""
        return _stub_response({"url": url})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
