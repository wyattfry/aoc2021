from typing import List
from aoc2021.solutionbase import SolutionBase


class Day07(SolutionBase):
    """
    --- Day 7: The Treachery of Whales ---
    https://adventofcode.com/2021/day/7
    """
    DAY: int = 7

    def __init__(self, puzzle_input: List[str]):
        self.puzzle_input = puzzle_input
        self.crab_positions = []
        self.crabs_at_position = {}
        self.computed = {}

    def setup(self):
        self.crabs_at_position = {}
        self.crab_positions = [int(x) for x in self.puzzle_input[0].split(',')]
        for c in self.crab_positions:
            if c in self.crabs_at_position:
                self.crabs_at_position[c] += 1
            else:
                self.crabs_at_position[c] = 1

    def get_fuel_to_position(self, current_position: int, crabs_at_position: int, target_position: int, corrected_calculation = False) -> int:
        if corrected_calculation:
            distance = abs(current_position - target_position)
            if distance not in self.computed:
                total_fuel = 0
                fuel_cost = 1
                for i in range(distance):
                    total_fuel += fuel_cost
                    fuel_cost += 1
                self.computed[distance] = total_fuel
            return self.computed[distance] * crabs_at_position
        else:
            return abs(crabs_at_position * target_position - crabs_at_position * current_position)

    def get_total_fuel_all_crabs_to_position(self, corrected_calculation = False) -> List[int]:
        min_pos = min(self.crabs_at_position.keys())
        max_pos = max(self.crabs_at_position.keys())
        fuel_sums = [0 for _ in range(min_pos, max_pos)]
        for pos in self.crabs_at_position.keys():
            for target_position in range(min_pos, max_pos):
                crabs_at_position = self.crabs_at_position[pos]
                fuel = self.get_fuel_to_position(pos, crabs_at_position, target_position, corrected_calculation)
                fuel_sums[target_position] += fuel
        return fuel_sums

    def part1(self):
        self.setup()
        fuel_sums = self.get_total_fuel_all_crabs_to_position()
        return min(fuel_sums)

    def part2(self):
        self.setup()
        """
        177225016 is too high
        """
        fuel_sums = self.get_total_fuel_all_crabs_to_position(corrected_calculation=True)
        return min(fuel_sums)
