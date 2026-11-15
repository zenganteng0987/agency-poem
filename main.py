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

POEM = """My brother, thirty-four, is too tall for the stool,
but he sits, and our mother stands behind him
with the kitchen scissors and an old sheet
printed with faded wedding roses.

The agent books him a barber —
a good one, it says — a chair that fits,
hot towels, eleven minutes.

He goes. He comes home with a haircut.
Then some Saturdays he is on the stool again,
knees up like a grasshopper,
saying the back itches — it doesn't —
just the back, then.

She cuts the way she has always cut:
too short over one ear, then evening up
makes the other side shorter,
and both agree the mirror
is a liar with an agenda.

The snip is the slowest sound in the house.
Hair on the sheet, hair on the floor,
her humming off-key through the thin places.

The agent keeps his calendar perfectly.
It has never swept a floor
and called the sweeping nothing.

He folds the sheet himself,
shakes the roses out in the yard,
and puts the stool back under the table —
too small, and exactly the right size.
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
