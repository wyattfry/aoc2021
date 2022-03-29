import argparse  # pragma: no cover
import os
import sys

from aoc2021.base import get_input
from aoc2021.day01 import Day01
from aoc2021.day02 import Day02
from aoc2021.day03 import Day03
from aoc2021.solution import Solution


def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m aoc2021` and `$ aoc2021 `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    parser = argparse.ArgumentParser(
        description="aoc2021.",
        epilog="Enjoy the aoc2021 functionality!",
    )
    # This is required positional argument
    parser.add_argument(
        "name",
        type=str,
        help="The username",
        default="wyattfry",
    )
    # This is optional named argument
    parser.add_argument(
        "-m",
        "--message",
        type=str,
        help="The Message",
        default="Hello",
        required=False,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Optionally adds verbosity",
    )
    args = parser.parse_args()
    print(f"{args.message} {args.name}!")
    if args.verbose:
        print("Verbose mode is on.")

    print("Executing main function")
    day = int(os.environ.get('DAY'))
    solution: Solution()
    puzzle_input = get_input(day)

    if day == 1:
        solution = Day01(puzzle_input)
    elif day == 2:
        solution = Day02(puzzle_input)
    elif day == 3:
        solution = Day03(puzzle_input)
    else:
        print('DAY env var not set')
        sys.exit(1)

    part1_answer = solution.part1()
    part2_answer = solution.part2()
    print(f'day {day}\npart 1 answer: {part1_answer}\npart 2 answer: {part2_answer}')
    # base = BaseClass()
    # print(base.base_method())
    # print(base_function())
    # print("End of main function")


if __name__ == "__main__":  # pragma: no cover
    main()
