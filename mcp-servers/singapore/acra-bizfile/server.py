"""MCP stub server: sg-acra-bizfile.

ACRA BizFile+ (bizfile.gov.sg). Returns SG company / business profiles.

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
        "server": "sg-acra-bizfile",
        "args": args,
        "result": {"uen": "201912345A", "name": "[STUB] Example Pte Ltd", "status": "Live", "officers": [{"name": "John Tan", "role": "Director"}]},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("sg-acra-bizfile")

    @mcp.tool()
    def lookup_company(uen: str = "", name: str = "") -> dict:
        """Look up a SG company by UEN or name."""
        return _stub_response({"uen": uen, "name": name})

    @mcp.tool()
    def list_officers(uen: str = "") -> dict:
        """List directors and secretaries of a UEN."""
        return _stub_response({"uen": uen})

    @mcp.tool()
    def list_charges(uen: str = "") -> dict:
        """List charges over a UEN's assets."""
        return _stub_response({"uen": uen})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
