"""MCP stub server: TianYanCha (天眼查).

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
        "server": "tianyancha-stub",
        "args": args,
        "result": {"profile": {"name": "[STUB] 示例公司", "uscc": "[STUB] 91110000XXXXXXXXXX", "capital": "[STUB] 1000万", "status": "存续", "litigation_count": 0, "ip_count": 0}},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("tianyancha-stub")

    @mcp.tool()
    def tyc_company(name: str = "") -> dict:
        """Pull a Chinese counter-party profile (registration, equity, litigation, IP, sanctions)."""
        return _stub_response({"name": name})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
