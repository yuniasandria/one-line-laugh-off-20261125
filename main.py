#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes exactly one funny line to /output/entry.txt.

Pure Python stdlib only. The line is assembled from two constants so the
full text is authored across two messages in the build session.
"""
import os

PART_A = "My smartwatch congratulated me on 10,000 steps, then my fridge filed a complaint: "
PART_B = "47 visits, zero salads."

LINE = PART_A + PART_B

assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} out of range"
assert LINE.strip(), "line must not be only whitespace"
assert "\n" not in LINE, "line must be a single line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
