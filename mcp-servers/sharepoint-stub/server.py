"""MCP stub server: SharePoint.

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
        "server": "sharepoint-stub",
        "args": args,
        "result": {"items": [{"id": "[STUB] sp-item-id", "name": "Sample doc.docx"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("sharepoint-stub")

    @mcp.tool()
    def sharepoint_call(site: str = "", action: str = "", library: str = "") -> dict:
        """Call a SharePoint (via Graph) endpoint."""
        return _stub_response({"site": site, "action": action, "library": library})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
