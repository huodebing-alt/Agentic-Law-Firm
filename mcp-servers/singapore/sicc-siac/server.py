"""MCP stub server: sg-sicc-siac.

SICC (sicc.gov.sg) and SIAC (siac.org.sg). Cause lists, awards summaries, rules.

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
        "server": "sg-sicc-siac",
        "args": args,
        "result": {"rules_version": "[STUB] SIAC Rules 2025", "url": "https://www.siac.org.sg/our-rules/rules"},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("sg-sicc-siac")

    @mcp.tool()
    def get_rules(body: str = "", version: str = "") -> dict:
        """Return current SICC or SIAC rules text."""
        return _stub_response({"body": body, "version": version})

    @mcp.tool()
    def get_cause_list(date: str = "") -> dict:
        """Return the SICC cause list for a date."""
        return _stub_response({"date": date})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
