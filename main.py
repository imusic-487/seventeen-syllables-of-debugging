#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging -- three lines in the 5-7-5 syllable
shape, at most 200 characters -- to /output/entry.txt.

Python 3.13 standard library only. No network, no input files, no
arguments: the haiku is fixed in this file, so every run writes the
exact same bytes.

The haiku:

    Cursor blinks at three
    the log line swears it worked here
    but the code moved on

The picture is concrete on purpose: a cursor blinking at three in the
morning, a log line insisting the code worked. The turn is the last
line -- the log is not lying, the code simply moved on since it ran,
so the truth it swears to is already stale.
"""

import os
import re
from pathlib import Path

HAIKU = (
    "Cursor blinks at three\n"
    "the log line swears it worked here\n"
    "but the code moved on"
)

EXPECTED_SYLLABLES = (5, 7, 5)


def count_syllables(word: str) -> int:
    """Rough syllable count for one lowercase word.

    Counts vowel groups, then takes off one for a silent trailing "e"
    ("code", "here", "moved") or a silent "-ed" after a consonant
    other than t/d ("worked"). Good enough for the three fixed lines
    here, and tested against their hand count below.
    """
    w = re.sub(r"[^a-z']", "", word.lower())
    if not w:
        return 0
    groups = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and groups > 1:
        groups -= 1
    elif w.endswith("ed") and len(w) > 2 and w[-3] not in "td":
        groups -= 1
    return max(1, groups)


def main() -> None:
    # Self-check against the competition gate before writing anything:
    # 1-200 characters, exactly three lines, not only whitespace.
    if not 1 <= len(HAIKU) <= 200:
        raise ValueError(f"haiku is {len(HAIKU)} characters, must be 1-200")
    lines = HAIKU.split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku has {len(lines)} lines, must be 3")
    if not HAIKU.strip():
        raise ValueError("haiku must not be only whitespace")
    # Self-check the 5-7-5 shape: hand-counted as
    # Cursor(2) blinks(1) at(1) three(1) = 5;
    # the(1) log(1) line(1) swears(1) it(1) worked(1) here(1) = 7;
    # but(1) the(1) code(1) moved(1) on(1) = 5.
    counts = tuple(
        sum(count_syllables(word) for word in line.split())
        for line in lines
    )
    if counts != EXPECTED_SYLLABLES:
        raise ValueError(
            f"syllable counts are {counts}, must be {EXPECTED_SYLLABLES}"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(HAIKU, encoding="utf-8")
    print(f"Wrote {len(HAIKU)} characters to {entry}")


if __name__ == "__main__":
    main()
