#!/usr/bin/env python3
"""generate-templates-extended.py — runs the multi-jurisdiction template generator.

Delegates to outputs/extend_part3.py for the SG + US templates.
For CN templates, see scripts/generate-templates.py (unchanged).
"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
EXTEND = ROOT / 'extend_part3.py'

if not EXTEND.exists():
    print('extend_part3.py not found; SG / US templates must be regenerated externally.')
    sys.exit(1)

subprocess.run([sys.executable, str(EXTEND)], check=True)
