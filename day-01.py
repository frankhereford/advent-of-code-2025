#!/usr/bin/env python3

import argparse
from pathlib import Path


def read_input(path: str | Path) -> list[str]:
    """Return trimmed lines from a relative or absolute path."""
    p = Path(path)
    text = p.read_text()
    return [line.strip() for line in text.splitlines()]


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
    lines = read_input(input_path)

    print(lines)


if __name__ == "__main__":
    main()
