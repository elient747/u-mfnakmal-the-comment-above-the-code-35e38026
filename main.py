#!/usr/bin/env python3
"""The Comment Above the Code — one original line, 1 to 200
characters, written as the comment a developer left above fragile
production code: funny because it is true.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
# Revised: the joke is that "temporary" code became permanent —
# it pays rent now, which is a fresher angle than who-wrote-this.
import os

# The entry line lives at module level so the content is separate
# from the file-writing logic below.
ENTRY_LINE = (
    "// This function has been \"temporary\" since 2019. "
    "It now pays rent, has a family, and outlived three rewrites."
)


def write_entry():
    line = ENTRY_LINE
    # Guard the bounty gate (1-200 characters) before writing, so a
    # future edit to the line fails loudly instead of silently.
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
