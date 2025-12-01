#!/usr/bin/env python3

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Advent of Code 2025 - Day 01")
    parser.add_argument(
        "--input",
        "-i",
        type=Path,
        required=True,
        help="Path to the puzzle input file",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path: Path = args.input

    print(f"Using input file: {input_path}")


if __name__ == "__main__":
    main()
