"""MCP stub server: Google Calendar.

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
        "server": "gcal-stub",
        "args": args,
        "result": {"events": [{"id": "[STUB] gcal-event-id", "summary": "Sample matter deadline"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("gcal-stub")

    @mcp.tool()
    def gcal_call(action: str = "", calendar_id: str = "") -> dict:
        """Call a Google Calendar API endpoint (list events, create, update)."""
        return _stub_response({"action": action, "calendar_id": calendar_id})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
