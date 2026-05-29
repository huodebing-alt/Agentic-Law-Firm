"""MCP stub server: sg-sso-statutes.

Singapore Statutes Online (sso.agc.gov.sg). Returns Acts and subsidiary legislation by short title or section.

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
        "server": "sg-sso-statutes",
        "args": args,
        "result": {"hits": [{"act": "Companies Act 1967", "section": "157", "text": "[STUB] Director's duty to act honestly and use reasonable diligence.", "in_force": true}]},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("sg-sso-statutes")

    @mcp.tool()
    def lookup_statute(query: str = "", section: str = "") -> dict:
        """Look up an SG Act or subsidiary legislation by short title, citation, or section."""
        return _stub_response({"query": query, "section": section})

    @mcp.tool()
    def list_in_force(topic: str = "") -> dict:
        """List currently in-force Acts in a topic area."""
        return _stub_response({"topic": topic})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
