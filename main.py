#!/usr/bin/env python3
"""One Letter for Your Day entry (make.fun program/v1).

Writes exactly one letter — "S" — to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``
(the grader mounts that directory at ``/output``).

The letter S stands for the word behind my day: sunrise. The day started
before the alarm, the sky already changing colour; S is also start, and
second chance — the day I get to begin again. One letter, nothing else.
"""

import os
import sys

LETTER = "S"


def main() -> int:
    # Gate guard: the entry must be exactly one letter, A to Z, and
    # nothing else — refuse to write anything that would fail the gate.
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        print(f"refusing to write invalid entry: {LETTER!r}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LETTER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
