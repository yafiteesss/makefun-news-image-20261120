#!/usr/bin/env python3
"""Write the finished Friday 20 November 2026 front page to /output/entry.png.

The picture lives in this repository; this program only places a copy
of it where the grader looks. No network, no randomness, and nothing
beyond the standard library.
"""
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
DST = Path("/output/entry.png")

DST.parent.mkdir(parents=True, exist_ok=True)
DST.write_bytes(SRC.read_bytes())
