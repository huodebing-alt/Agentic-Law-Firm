"""Common helpers for MCP stub servers.

Real backends should replace `_stub_response` with their actual API
calls. This module exists so we can keep all stub servers small.
"""
from __future__ import annotations
import json


def stub_response(server: str, args: dict, sample_result: dict) -> dict:
    return {
        "status": "stub",
        "server": server,
        "args": args,
        "result": sample_result,
        "note": "Replace with real backend; see README.md alongside this server.",
    }
