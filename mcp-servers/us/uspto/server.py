"""MCP stub server: us-uspto.

USPTO TSDR (trademarks) and PatentsView (patents). Free public APIs.

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
        "server": "us-uspto",
        "args": args,
        "result": {"hits": [{"serial": "[STUB] 88123456", "mark": "EXAMPLEMARK", "status": "Live", "class": "009"}]},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("us-uspto")

    @mcp.tool()
    def search_trademark(mark: str = "", nice_class: str = "") -> dict:
        """Search USPTO TSDR by mark / class."""
        return _stub_response({"mark": mark, "nice_class": nice_class})

    @mcp.tool()
    def get_trademark_status(serial_no: str = "") -> dict:
        """Get trademark status by serial number."""
        return _stub_response({"serial_no": serial_no})

    @mcp.tool()
    def search_patents(query: str = "") -> dict:
        """Search PatentsView for patents."""
        return _stub_response({"query": query})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
