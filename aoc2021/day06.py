from typing import List
from aoc2021.solutionbase import SolutionBase


class Day06(SolutionBase):
    """
    --- Day 6: Lanternfish ---
    https://adventofcode.com/2021/day/6
    """
    DAY: int = 6

    def __init__(self, puzzle_input: List[str]):
        self.puzzle_input = puzzle_input
        self.lanternfish_school = {}
        self.fish_day: int = 0

    def get_school_size(self):
        return sum(self.lanternfish_school.values())

    def parse_puzzle_input(self):
        fish_list: List[int] = [int(x) for x in self.puzzle_input[0].split(',')]
        for f in fish_list:
            self.lanternfish_school[f] += 1

    def setup(self):
        # lanternfish_school is a dictionary, where fish are grouped
        # by their current day in their life cycle, the keys represent
        # the day (0-8), the values represent the number of fish at
        # that day.
        self.lanternfish_school = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0
        }
        self.fish_day: int = 0
        self.parse_puzzle_input()

    def simulate_fish_day(self):
        zero_day_fish_count = self.lanternfish_school[0]
        for i in range(1, len(self.lanternfish_school)):
            self.lanternfish_school[i - 1] = self.lanternfish_school[i]
        self.lanternfish_school[6] += zero_day_fish_count
        self.lanternfish_school[8] = zero_day_fish_count

    def simulate_n_fish_days(self, sim_days: int) -> None:
        for _ in range(sim_days):
            self.simulate_fish_day()

    def part1(self):
        self.setup()
        self.simulate_n_fish_days(80)
        return self.get_school_size()

    def part2(self):
        self.setup()
        self.simulate_n_fish_days(256)
        return self.get_school_size()
