"""MCP stub server: Google Drive.

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
        "server": "gdrive-stub",
        "args": args,
        "result": {"files": [{"id": "[STUB] gdrive-file-id", "name": "Sample SPA.docx"}]},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("gdrive-stub")

    @mcp.tool()
    def gdrive_call(action: str = "", query: str = "") -> dict:
        """Call a Google Drive API endpoint (list / get / upload)."""
        return _stub_response({"action": action, "query": query})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
