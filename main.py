#!/usr/bin/env python3
"""Write one wedding vow from a robot to /output/entry.txt."""

from pathlib import Path

VOW = "I vow to love you through every update, every reboot, and every low-battery warning — until death, or a factory reset, do us part."

ENTRY = Path("/output/entry.txt")


def main() -> None:
    assert len(VOW) <= 200, "vow must fit the 200-character limit"
    ENTRY.parent.mkdir(parents=True, exist_ok=True)
    ENTRY.write_text(VOW + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
