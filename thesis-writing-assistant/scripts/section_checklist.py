#!/usr/bin/env python3
from __future__ import annotations

import argparse


CHECKLISTS = {
    "abstract": [
        "state the problem",
        "state the method",
        "state the main result",
        "state the contribution",
    ],
    "related-work": [
        "group prior work by theme",
        "compare rather than list",
        "state the gap",
        "link the gap to your work",
    ],
    "method": [
        "define inputs and outputs",
        "state assumptions",
        "make steps reproducible",
        "name hyperparameters or settings that matter",
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Print a revision checklist for an academic section.")
    parser.add_argument("section", choices=sorted(CHECKLISTS), help="Section type.")
    args = parser.parse_args()
    for item in CHECKLISTS[args.section]:
        print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
