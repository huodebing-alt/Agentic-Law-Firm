"""MCP stub server: Zoom.

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
        "server": "zoom-stub",
        "args": args,
        "result": {"meeting_id": "[STUB] zoom-meeting-id", "join_url": "https://zoom.us/j/..."},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("zoom-stub")

    @mcp.tool()
    def zoom_call(action: str = "", topic: str = "") -> dict:
        """Call a Zoom API endpoint (create meeting, list recordings)."""
        return _stub_response({"action": action, "topic": topic})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
