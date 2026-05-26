#!/usr/bin/env python3
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Markdown research plan template.")
    parser.add_argument("topic", help="Research topic or idea.")
    args = parser.parse_args()

    print(f"# Research Plan: {args.topic}\n")
    print("## Research Question\n- \n")
    print("## Hypothesis\n- \n")
    print("## Proposed Method\n- \n")
    print("## Baselines\n- \n")
    print("## Data\n- \n")
    print("## Metrics\n- \n")
    print("## Risks\n- \n")
    print("## Next 7 Days\n- \n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
