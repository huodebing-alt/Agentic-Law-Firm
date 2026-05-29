"""MCP stub server: sg-ipos.

Intellectual Property Office of Singapore (ipos.gov.sg). Trademark / patent / design / copyright search.

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
        "server": "sg-ipos",
        "args": args,
        "result": {"hits": [{"application_no": "40201900001A", "mark": "[STUB] EXAMPLEMARK", "owner": "Example Pte Ltd", "status": "Registered"}]},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("sg-ipos")

    @mcp.tool()
    def search_trademark(mark: str = "", nice_class: str = "") -> dict:
        """Search the IPOS trademark register."""
        return _stub_response({"mark": mark, "nice_class": nice_class})

    @mcp.tool()
    def search_patent(query: str = "") -> dict:
        """Search the IPOS patent register."""
        return _stub_response({"query": query})

    @mcp.tool()
    def get_application_status(application_no: str = "") -> dict:
        """Get the status of a filing."""
        return _stub_response({"application_no": application_no})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
