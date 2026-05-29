"""MCP stub server: sg-iras.

Inland Revenue Authority of Singapore (iras.gov.sg). Tax guides, advance rulings, GST register.

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
        "server": "sg-iras",
        "args": args,
        "result": {"hits": [{"title": "[STUB] e-Tax Guide on GST", "url": "https://www.iras.gov.sg/...", "published": "2024-03-01"}]},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("sg-iras")

    @mcp.tool()
    def search_guides(query: str = "") -> dict:
        """Search IRAS e-Tax Guides."""
        return _stub_response({"query": query})

    @mcp.tool()
    def get_gst_registration(uen: str = "") -> dict:
        """Check GST registration status by UEN."""
        return _stub_response({"uen": uen})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
