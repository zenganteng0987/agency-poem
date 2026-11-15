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

POEM = """The clock in the hall was my mother's wedding present
to herself, she used to say —
bought with her first wages,
wound every Sunday of her marriage.

The agent offers to keep it true.
It knows the second the year turns over.
It can set the hands from anywhere,
and has. Twice. While he slept.

He unwound that with his own hands,
four minutes fast, the way she kept it,
and stood there breathing with it
like a man who has won an argument
with nobody in the room.

Four minutes is not much.
It is one song on the radio.
It is the kettle, almost.
It is the whole of his lateness
arriving early, on purpose.

Sundays he opens the glass,
fits the small key, turns it
seven times, no more —
the spring complains, the pendulum
remembers its road.

The agent keeps the house to the second.
His clock is four minutes fast,
and entirely his.
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
