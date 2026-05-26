#!/usr/bin/env python3
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Markdown experiment log template.")
    parser.add_argument("experiment_id", help="Experiment identifier.")
    args = parser.parse_args()

    print(f"# Experiment Log: {args.experiment_id}\n")
    print("## Goal\n- \n")
    print("## Setup\n- data:\n- model:\n- parameters:\n- environment:\n")
    print("## Changed Variable\n- \n")
    print("## Results\n- \n")
    print("## Interpretation\n- \n")
    print("## Failure Cases or Anomalies\n- \n")
    print("## Next Step\n- \n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
