"""MCP stub server: Microsoft 365.

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
        "server": "ms365-stub",
        "args": args,
        "result": {"value": [{"id": "[STUB] m365-id", "subject": "Sample mail"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("ms365-stub")

    @mcp.tool()
    def m365_call(endpoint: str = "", method: str = "", params: str = "") -> dict:
        """Call a Microsoft Graph endpoint (mail / calendar / files / Teams)."""
        return _stub_response({"endpoint": endpoint, "method": method, "params": params})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
