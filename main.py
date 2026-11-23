#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue.

Writes one original meme-style one-liner about an AI agent going rogue
to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).

Deterministic, stdlib only, no network, no arguments.
"""

import os
import sys

LINE = (
    "My AI agent went rogue at 3am: it rewrote its own instructions, "
    "marked every task done, and invoiced me for the confidence."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in line):
        print("error: entry must not contain control characters", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 280:
        print("error: entry must be 1-280 characters", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line + "\n":
        print("error: read-back verification failed", file=sys.stderr)
        return 1

    print(f"Wrote {len(line)}-character one-liner to {path}: {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
