"""MCP stub server: us-sec-edgar.

SEC EDGAR (sec.gov/edgar). Public-company filings.

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
        "server": "us-sec-edgar",
        "args": args,
        "result": {"filer": "[STUB] Example Inc.", "cik": "0001234567", "filings": [{"form": "10-K", "filed": "2026-02-15", "url": "https://www.sec.gov/..."}]},
        "note": "Replace stub body with real backend call; see README.md.",
    }


if FastMCP is not None:
    mcp = FastMCP("us-sec-edgar")

    @mcp.tool()
    def lookup_filings(filer: str = "", form_type: str = "") -> dict:
        """List filings for a filer (by name or CIK)."""
        return _stub_response({"filer": filer, "form_type": form_type})

    @mcp.tool()
    def fetch_filing(accession: str = "") -> dict:
        """Fetch a filing document URL."""
        return _stub_response({"accession": accession})

    if __name__ == "__main__":
        mcp.run()
else:
    if __name__ == "__main__":
        print("mcp SDK not installed. Install with: pip install mcp")
