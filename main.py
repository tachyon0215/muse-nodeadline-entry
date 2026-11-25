#!/usr/bin/env python3
"""Write the no-deadline-met excuse entry to entry.txt.

Judging fit: the competition asks for one line from someone who
missed a deadline, so the line has to sound like a real, cornered
excuse rather than a joke about deadlines in general. This entry is
self-defeating in a believable way: the work was finished on time,
then three days went into rewriting its first line so it would not
look rushed. The punch lands in the final words, because the effort
to hide haste is exactly what caused the delay being apologised for.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Sorry it's late - I finished it on time, then spent three days rewriting the first line so it wouldn't look rushed."
TEXT = LINE + "\n"
MAX_CHARS = 200
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")
    if body != body.strip():
        raise ValueError("no leading or trailing whitespace")
    if not body.endswith("."):
        raise ValueError("entry should end with a full stop")
    if "  " in body:
        raise ValueError("no double spaces")
    if any(not ch.isprintable() for ch in body):
        raise ValueError("entry must be printable text only")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
