"""MCP stub server: Microsoft Teams.

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
        "server": "teams-stub",
        "args": args,
        "result": {"value": [{"id": "[STUB] team-id", "displayName": "Matters Team"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("teams-stub")

    @mcp.tool()
    def teams_call(action: str = "") -> dict:
        """Call a Microsoft Teams (Graph) endpoint."""
        return _stub_response({"action": action})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
