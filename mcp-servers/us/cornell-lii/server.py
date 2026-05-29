"""MCP stub server: us-cornell-lii.

Cornell Law - Legal Information Institute (law.cornell.edu). USC, CFR, FRCP, state codes.

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
        "server": "us-cornell-lii",
        "args": args,
        "result": {"citation": "26 USC 482", "title": "Allocation of income and deductions among taxpayers", "text": "[STUB] Section text..."},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("us-cornell-lii")

    @mcp.tool()
    def lookup_statute(citation: str = "") -> dict:
        """Look up a US statute (USC title-section, CFR title-part, or named state code)."""
        return _stub_response({"citation": citation})

    @mcp.tool()
    def lookup_regulation(citation: str = "") -> dict:
        """Look up a CFR title-section regulation."""
        return _stub_response({"citation": citation})

    @mcp.tool()
    def lookup_rule(rule: str = "") -> dict:
        """Look up an FRCP / FRE / FRAP rule."""
        return _stub_response({"rule": rule})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
