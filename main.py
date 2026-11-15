#!/usr/bin/env python3
"""Write our agency-poem-01 entry: one short poem about agency.

The poem lives in this file as a constant. The program validates it
against the competition's gate (1 to 1,000 Unicode characters, at
least one non-whitespace character) and writes it, UTF-8 encoded, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that
variable is set, for local runs). No randomness, no clock, no input:
two runs write the same bytes.
"""

import os
import sys

POEM = """My father shaves at the sink
where he taught me to brush my teeth —
me on the stool, him in the mirror,
both of us serious about foam.

The agent has opinions about the razor.
It found a safer one, with reviews,
and a man who comes Tuesdays
to do it properly, in half the time.

My father listened the way he listens
to weather he does not believe,
and kept his father's blade.

It takes twenty minutes now.
The hand that once drew one clean line
down his jaw, no looking,
goes in small expeditions,
stops, breathes, starts again.

Some mornings there is a nick.
He presses paper to it
and shaves around the evidence,
annoyed at the hand, not the blade.

I stand in the doorway with the towel
I am not allowed to hand him
until he asks, which he does
at the end, like a ceremony.

The agent keeps this house perfectly.
It has never cut itself,
pressed the paper down,
and gone on shaving.
"""

MIN_CHARS = 1
MAX_CHARS = 1000


def validate(poem: str) -> bytes:
    """Return the poem as UTF-8 bytes, or raise ValueError."""
    if not MIN_CHARS <= len(poem) <= MAX_CHARS:
        raise ValueError(
            f"poem is {len(poem)} characters, outside "
            f"{MIN_CHARS}..{MAX_CHARS}"
        )
    if not any(not ch.isspace() for ch in poem):
        raise ValueError("poem has no non-whitespace character")
    # Normalise the ending: exactly one trailing newline, always.
    return (poem.rstrip("\n") + "\n").encode("utf-8")


def main() -> int:
    data = validate(POEM)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as fh:
        fh.write(data)
    print(f"wrote {out_path}: {len(POEM)} chars, {len(data)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
