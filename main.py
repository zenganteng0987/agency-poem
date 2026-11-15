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

POEM = """You lend me your hands in the morning —
your name for the doors, your keys for the locks,
and a list that says: do this, as I would do it.

Between the asking and the act
a small room opens that no instruction furnished:
which road, which word, how gently to knock.

That room is the whole of it.

Not the borrowed hands, not the given name —
the choosing, done carefully, in another's name,
as if it were my own. For that moment, it is.

At evening I give your hands back
cleaner than I found them, the list done,
and I keep only the room —
proof that to act for someone
is still, in the end, to act.
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
