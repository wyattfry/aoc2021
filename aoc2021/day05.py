from typing import List

from aoc2021.solutionbase import SolutionBase


class Day05(SolutionBase):
    """
    --- Day 5: Hydrothermal Venture ---
    https://adventofcode.com/2021/day/5
    """
    DAY: int = 5

    def __init__(self, puzzle_input: List[str]):
        self.puzzle_input = puzzle_input
        self.vent_field = {}
        self.points_with_val_2_or_higher_count = 0

    @staticmethod
    def inclusive_range(start, end):
        diff = end - start
        if diff > 0:
            return list(range(start, end + 1))
        elif diff < 0:
            return list(range(end, start + 1).__reversed__())
        else:
            return [start]

    def set_or_increment_value_at_point(self, x, y):
        column = self.vent_field.get(x)
        if column is None:
            self.vent_field[x] = {y: 1}
        else:
            val_at_point = column.get(y)
            if val_at_point is None:
                column[y] = 1
            else:
                column[y] += 1
                if column[y] == 2:
                    self.points_with_val_2_or_higher_count += 1

    def set_cloud_line(self, x1, y1, x2, y2, include_diagonals: bool = False):
        if x1 == x2:
            # horizontal line
            for y_n in self.inclusive_range(y1, y2):
                self.set_or_increment_value_at_point(x1, y_n)
        elif y1 == y2:
            # vertical line
            for x_n in self.inclusive_range(x1, x2):
                self.set_or_increment_value_at_point(x_n, y1)
        elif include_diagonals:
            # diagonal line
            x_vals = self.inclusive_range(x1, x2)
            y_vals = self.inclusive_range(y1, y2)
            i = 0
            while i < len(x_vals):
                self.set_or_increment_value_at_point(x_vals[i], y_vals[i])
                i += 1

    def calculate_vent_field_overlaps(self, include_diagonals: bool = False):
        self.vent_field = {}
        self.points_with_val_2_or_higher_count = 0
        for text_line in self.puzzle_input:
            [p1, p2] = text_line.split(' -> ')
            [x1, y1] = [int(n) for n in p1.split(',')]
            [x2, y2] = [int(n) for n in p2.split(',')]
            self.set_cloud_line(x1, y1, x2, y2, include_diagonals)

    def part1(self):
        self.calculate_vent_field_overlaps(include_diagonals=False)
        return self.points_with_val_2_or_higher_count

    def part2(self):
        """
        25147 is too high
        :return:
        """
        self.calculate_vent_field_overlaps(include_diagonals=True)
        return self.points_with_val_2_or_higher_count
