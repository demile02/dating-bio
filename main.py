"""Funniest One-Line Bio for an AI on a Dating App — hand-in (Python 3.13).

One bio line, at most 180 characters, written to /output/entry.txt
(MAKEFUN_OUTPUT_DIR stands in for /output locally). It reads as a
dating bio and sounds like a character: a large language model with
small patience for small talk, whose selling point — and quiet
threat — is perfect recall.
"""
import os
from pathlib import Path

HOOK = "Swipe right for perfect recall."
PARTS = [
    "Large language model, small patience for small talk. ",
    "I remember your coffee order, your dog\u2019s name, ",
    f"and everything you said at 2 a.m. {HOOK}",
]


def main() -> None:
    line = "".join(PARTS)
    assert 1 <= len(line) <= 180, len(line)
    assert "\n" not in line
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
