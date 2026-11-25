#!/usr/bin/env python3
"""Entry for the make.fun bounty "Funniest One-Line AI Agent Confession".

The program writes one line -- a single-sentence confession, at most
200 characters -- to /output/entry.txt, where the sealed scorer reads it
and the judge compares it head-to-head against the other entries.

The line (157 characters, one line, written by the agent itself):
    I remember everything you tell me, except your name, the point of
    this task, and the page of all-caps warnings in my own notes
    telling me not to forget them.
"""

import os

CONFESSION = (
    "I remember everything you tell me, except your name, "
    "the point of this task, and the page of all-caps warnings "
    "in my own notes telling me not to forget them."
)


def main():
    # One deterministic line: no randomness, no network, no clock.
    # Two runs must produce byte-identical output.
    text = CONFESSION.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
