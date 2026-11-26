#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the house cat's one-sentence excuse for the glass it just swept
off the table to /output/entry.txt, exactly as the program/v1 harness
requires: one sentence, UTF-8, 1 to 200 characters, no apology, no
confession, just the cat's own case for itself.

Pure standard library, deterministic: the same text on every run.
"""

import os
import sys

ENTRY = "That glass squatted rent-free in my sunbeam all afternoon, so I evicted it."

# The cat's logic: the sunbeam is its territory, the glass was a squatter,
# and eviction is a property matter, not an accident. No remorse anywhere.

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
