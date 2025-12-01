#!/usr/bin/env python3

import argparse
import re
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


INSTRUCTION_PATTERN = re.compile(r"^(\w)(\d+)$")


def process_instructions(
    initial_position: int = 50, instructions: list[str] | None = None
) -> None:
    """Print each instruction and parse it into its components.

    Args:
        initial_position: Starting position value (currently unused, defaults to 50).
        instructions: List of instruction strings to process.
    """
    if instructions is None:
        instructions = []

    for instruction in instructions:
        match = INSTRUCTION_PATTERN.match(instruction)
        if not match:
            print(f"Unrecognized instruction format: {instruction!r}")
            continue

        letter, number_str = match.groups()
        number = int(number_str)

        print(f"instruction={instruction!r}, letter={letter!r}, number={number}")


def main() -> None:
    args = parse_args()
    input_path: Path = args.input

    print(f"Using input file: {input_path}")
    lines = read_input(input_path)

    process_instructions(instructions=lines)


if __name__ == "__main__":
    main()
