#!/usr/bin/env python3
"""Put the finished Friday 20 November 2026 front page at /output/entry.png.

The picture is stored in this repository; this program only moves it
into place. Standard library only, no network, no randomness.
"""
from pathlib import Path
import shutil

HERE = Path(__file__).resolve().parent
OUT = Path("/output/entry.png")

OUT.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT)
