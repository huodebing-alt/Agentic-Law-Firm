"""MCP stub server: Slack.

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
        "server": "slack-stub",
        "args": args,
        "result": {"ok": true, "ts": "[STUB] slack-message-ts"},
        "note": "Replace with real backend; see README.md alongside this server.",
    }


if FastMCP is not None:
    mcp = FastMCP("slack-stub")

    @mcp.tool()
    def slack_call(action: str = "", channel: str = "", text: str = "") -> dict:
        """Call a Slack API endpoint (post message, list channels, fetch history)."""
        return _stub_response({"action": action, "channel": channel, "text": text})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
