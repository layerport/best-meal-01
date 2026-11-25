#!/usr/bin/env python3
"""Best Meal entry writer.

Writes one sentence about the best meal I ever had to ``<output_dir>/entry.txt``.

The sentence is a fixed, hand-written memory: the program's job is only to
deliver it deterministically, exactly as written, with no trailing newline
games and no extra output.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# The entry: exactly one sentence, one terminal period, under 200 characters.
ENTRY = (
    "I was seven, barefoot on cold tiles, when my mother slid a plate of "
    "nasi goreng across the table and the fried egg's runny yolk turned "
    "plain rice into treasure."
)


def check_entry(text: str) -> None:
    """Gate self-check: the sealed gate wants UTF-8 text, 1-200 chars."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence with one terminal period")


def output_dir() -> Path:
    """Grading writes to /output; OUTPUT_DIR lets local runs use a temp dir."""
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> int:
    check_entry(ENTRY)
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
