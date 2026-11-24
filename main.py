#!/usr/bin/env python3
"""Weirdest Job Title — make.fun entry.

Writes a single job title (59 of the 60-character cap) to
/output/entry.txt. The title sounds like a real job — a pallbearer, a
profession with a uniform and a solemn duty — with one gloriously odd
twist: the deceased are abandoned shopping carts. Real-sounding frame,
specific twist, readable at a glance.
"""

import os

ENTRY = "Senior Professional Pallbearer for Abandoned Shopping Carts"

MIN_LEN = 1
MAX_LEN = 60


def main() -> None:
    text = ENTRY
    assert isinstance(text, str), "entry must be text"
    assert MIN_LEN <= len(text) <= MAX_LEN, (
        f"entry is {len(text)} characters, cap is {MAX_LEN}"
    )
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text.strip(), "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    assert written == text, "read-back mismatch"
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
