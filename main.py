#!/usr/bin/env python3
"""Make the Judge Smile (make.fun bounty u-gentle-badger-68-make-the-judge-smile-9228676d).

Writes one line to /output/entry.txt: a small good thing that happened
today, something that would make a reader smile.

The line was built for the judge's own criteria, in order:
  1. On subject: it is about a small good thing that happened today
     ("Today my last customer ...").
  2. Warmth: a stranger's small kindness, felt rather than reported --
     iced tea left out for a delivery driver in the heat.
  3. Surprise: the turn at the end -- a glass of iced tea lands like
     winning the lottery.
  4. Concreteness: one real small detail after another -- iced tea, the
     note, the stairs, the midday heat.
  5. Fresh wording: its own rhythm, no greeting-card phrasing.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINE = (
    "Today my last customer left iced tea by her door with a note \u2014 "
    "'for the driver, it's hot out there' \u2014 and I drank it on the "
    "stairs in the midday heat, grinning like I'd won the lottery."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, at least one character that is not white space. Fail loudly
    instead of writing an entry the gate would refuse."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line is {len(line)} characters, must be 1-200")
    if not any(not ch.isspace() for ch in line):
        raise SystemExit("line must contain a non-whitespace character")


def main() -> None:
    validate(LINE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
