"""MCP stub server: OneDrive.

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
        "server": "onedrive-stub",
        "args": args,
        "result": {"files": [{"id": "[STUB] onedrive-file-id", "name": "Sample doc.docx"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("onedrive-stub")

    @mcp.tool()
    def onedrive_call(action: str = "", path: str = "") -> dict:
        """Call a OneDrive (via Graph) endpoint."""
        return _stub_response({"action": action, "path": path})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
