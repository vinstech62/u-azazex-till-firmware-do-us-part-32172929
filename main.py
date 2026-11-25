#!/usr/bin/env python3
"""Till Firmware Do Us Part — write the robot's wedding vow to /output/entry.txt."""

import os

VOW = "I vow to love you through every update, every reboot, and every low-battery warning \u2014 until death, or a factory reset, do us part."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
