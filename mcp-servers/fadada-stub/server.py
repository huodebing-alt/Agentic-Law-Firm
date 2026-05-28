"""MCP stub server: FaDaDa (法大大).

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
        "server": "fadada-stub",
        "args": args,
        "result": {"task_id": "[STUB] fdd-task-12345", "status": "sent"},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("fadada-stub")

    @mcp.tool()
    def fdd_send(file_path: str = "", recipients: str = "") -> dict:
        """Send a document for e-signature via FaDaDa."""
        return _stub_response({"file_path": file_path, "recipients": recipients})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
