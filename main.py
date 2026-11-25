#!/usr/bin/env python3
"""Write one single-line joke excusing a missed deadline to /output/entry.txt.

The line is a fixed, hand-written string: no randomness, no network, no input,
so every run writes byte-identical output.
"""

from pathlib import Path

LINE = "I treated the deadline like a software update and kept clicking 'remind me tomorrow' until tomorrow ran out of tomorrows."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Enforce the bounty gate before writing: 1-200 characters, one line.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} characters, must be 1-200")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
