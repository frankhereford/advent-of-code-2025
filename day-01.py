#!/usr/bin/env python3

import argparse
import logging
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
logger = logging.getLogger(__name__)


def process_instructions(
    initial_position: int = 50, instructions: list[str] | None = None
) -> tuple[int, int]:
    """Print each instruction, update the dial, and count zeros.

    Args:
        initial_position: Starting dial position (defaults to 50).
        instructions: List of instruction strings to process.
    Returns:
        tuple[int, int]: A tuple `(zeros_by_instructions, zeros_by_clicks)` where:
            - `zeros_by_instructions` is how many instructions end on position 0.
            - `zeros_by_clicks` is how many individual clicks land on position 0.
    """
    if instructions is None:
        instructions = []

    dial_position = initial_position
    logger.info("Dial position: %s", dial_position)

    zero_by_clicks = 0
    zero_by_instructions = 0

    for instruction in instructions:
        match = INSTRUCTION_PATTERN.match(instruction)
        if not match:
            logger.warning("Unrecognized instruction format: %r", instruction)
            continue

        letter, number_str = match.groups()
        number = int(number_str)

        logger.debug(
            "instruction=%r, letter=%r, number=%d", instruction, letter, number
        )

        for number in range(number):
            if letter == "L":
                dial_position -= 1
            elif letter == "R":
                dial_position += 1
            else:
                raise

            dial_position = (dial_position) % 100

            if not dial_position:
                zero_by_clicks += 1

            logger.debug(
                "position: %s, instructions: %s, clicks: %s",
                dial_position,
                zero_by_instructions,
                zero_by_clicks,
            )

        if not dial_position:
            zero_by_instructions += 1

    return (zero_by_instructions, zero_by_clicks)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    args = parse_args()
    input_path: Path = args.input

    logger.info("Using input file: %s", input_path)
    lines = read_input(input_path)

    zeros = process_instructions(instructions=lines)
    logger.info("Zeros by instructions: %d and zeros by clicks: %d", zeros[0], zeros[1])


if __name__ == "__main__":
    main()
