from aoc2021.solution import Solution


class Day01(Solution):
    def __init__(self, input):
        self.input = [int(i) for i in input]

    def part1(self) -> int:
        """
        How many measurements are larger than the previous measurement?
        """
        previous = None
        count = 0
        for i in self.input:
            if previous and previous < i:
                count += 1
            previous = i
        print(f"Part 1: increase count: {count}")
        return count

    def part2(self) -> int:
        """
        Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
        """
        count = 0
        i = 0
        while i < len(self.input):
            try:
                current_window = sum([self.input[i - 0], self.input[i - 1], self.input[i - 2]])
                next_window = sum([self.input[i + 1], self.input[i - 0], self.input[i - 1]])
                count += 1 if next_window > current_window else 0
            except IndexError:
                print('swallowing index error')
            i += 1
        return count