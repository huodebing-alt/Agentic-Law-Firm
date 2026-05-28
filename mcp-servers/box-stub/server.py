"""MCP stub server: Box.

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
        "server": "box-stub",
        "args": args,
        "result": {"items": [{"id": "[STUB] box-item-id", "name": "Sample doc.docx"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("box-stub")

    @mcp.tool()
    def box_call(action: str = "", folder_id: str = "") -> dict:
        """Call a Box API endpoint."""
        return _stub_response({"action": action, "folder_id": folder_id})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
