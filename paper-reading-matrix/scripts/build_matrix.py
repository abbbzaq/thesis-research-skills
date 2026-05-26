#!/usr/bin/env python3
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Markdown paper reading matrix template.")
    parser.add_argument("papers", nargs="+", help="Paper titles or short identifiers.")
    args = parser.parse_args()

    headers = [
        "Paper",
        "Problem",
        "Method",
        "Dataset",
        "Metrics",
        "Main Result",
        "Limitation",
        "Relevance",
    ]
    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join(["---"] * len(headers)) + " |")
    for paper in args.papers:
        print("| " + " | ".join([paper, "", "", "", "", "", "", ""]) + " |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
