from aoc2021.solution import Solution


class Day02(Solution):
    day: int = 2
    """--- Day 2: Dive! ---"""

    def __init__(self, puzzle_input):
        self.input = puzzle_input

    def part1(self) -> int:
        """
        How many measurements are larger than the previous measurement?
        """
        horizontal_position = 0
        vertical_position = 0
        for i in self.input:
            [direction, amount] = i.split(' ')
            amount = int(amount)
            horizontal_position += amount if direction == "forward" else 0
            vertical_position += amount if direction == "down" else 0
            vertical_position -= amount if direction == "up" else 0
        return horizontal_position * vertical_position

    def part2(self) -> int:
        """
        down X increases your aim by X units.
        up X decreases your aim by X units.
        forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.
        """
        aim = 0
        horizontal_position = 0
        vertical_position = 0
        for i in self.input:
            [direction, amount] = i.split(' ')
            amount = int(amount)
            horizontal_position += amount if direction == "forward" else 0
            vertical_position += amount * aim if direction == "forward" else 0
            aim += amount if direction == "down" else 0
            aim -= amount if direction == "up" else 0
        return horizontal_position * vertical_position
