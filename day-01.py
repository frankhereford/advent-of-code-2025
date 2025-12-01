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
) -> int:
    """Print each instruction and parse it into its components.

    Args:
        initial_position: Starting position value (currently unused, defaults to 50).
        instructions: List of instruction strings to process.
    Returns:
        zeros: Integer count (currently unused placeholder, always 0).
    """
    if instructions is None:
        instructions = []

    zeros = 0

    dial_position = initial_position
    print(f"Dial position: {dial_position}")

    for instruction in instructions:
        match = INSTRUCTION_PATTERN.match(instruction)
        if not match:
            print(f"Unrecognized instruction format: {instruction!r}")
            continue

        letter, number_str = match.groups()
        number = int(number_str)

        print(f"instruction={instruction!r}, letter={letter!r}, number={number}")

        # part 1 solution

        # if letter == "L":
        #     dial_position -= number
        # elif letter == "R":
        #     dial_position += number
        # else:
        #     print(f"Unrecognized letter: {letter!r}")
        #     continue

        # dial_position = (dial_position) % 100

        # print(f"Dial position: {dial_position}")
        # if not dial_position:
        #     zeros += 1
        #     print(f"Got a zero, up to {zeros} zeros.")

    return zeros


def main() -> None:
    args = parse_args()
    input_path: Path = args.input

    print(f"Using input file: {input_path}")
    lines = read_input(input_path)

    zeros = process_instructions(instructions=lines)
    print(f"Zeros found: {zeros}")


if __name__ == "__main__":
    main()
