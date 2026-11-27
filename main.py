#!/usr/bin/env python3
"""One Word for the Boss — writes exactly one word to /output/entry.txt.

The boss, in one word: Gasbag.

Why this word: the boss talks — long meetings, longer monologues, and
every "quick sync" turns into a sermon while the actual work waits.
Gasbag is the word a colleague mutters at lunch after the third
all-hands of the week, and everyone at the table laughs because they
have all sat through the same hot air. It is funny on its own, it
rings true about a real boss habit, and it is not the first word
anyone reaches for.
"""

import os

WORD = "Gasbag"


def validate(word):
    """Gate mirror: UTF-8 text, 1-30 chars, exactly one word, not blank."""
    assert isinstance(word, str) and word.strip() == word and word
    assert len(word) <= 30 and " " not in word and "\n" not in word


def main():
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    # Self-check gate: what was written must be exactly the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == WORD


if __name__ == "__main__":
    main()
