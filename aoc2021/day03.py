from typing import List

from aoc2021.solution import Solution


class Day03(Solution):
    """
    --- Day 3: Binary Diagnostic ---
    https://adventofcode.com/2021/day/3
    """
    day: int = 3
    gamma_rate: int = 0
    co2_scrubber_rating: int = 0
    o2_generator_rating: int = 0

    def __init__(self, puzzle_input):
        self.input = [int(x, 2) for x in puzzle_input]
        self.digits = len(puzzle_input[0].strip())

    @staticmethod
    def get_whether_one_place(number: int, place: int) -> bool:
        # given a `number`, e.g. 4 or 00100
        # and a `place` i.e. binary exponent, 0 for unit, 1 for 2, 2 for 4 etc
        # return whether 1 or 0
        return 2 ** place == 2 ** place & number

    @staticmethod
    def get_whether_more_ones(numbers) -> bool:
        length = len(numbers)
        ones_count = 0
        for n in numbers:
            if n < 0 or n > 1:
                raise RuntimeError(f'received a number other than 1 or 0: {n}')
            ones_count += n
            if ones_count > length / 2:

                return True
        return False

    def get_gamma_rate(self):
        gamma_rate = 0
        for place in range(self.digits):
            column: List[int] = [
                int(Day03.get_whether_one_place(number, place))
                for number in self.input
            ]
            more_ones: bool = Day03.get_whether_more_ones(column)
            gamma_rate += 2 ** place if more_ones else 0
            self.gamma_rate = gamma_rate
        return gamma_rate

    @staticmethod
    def get_inverse(num: int, mask_size: int):
        return (1 << mask_size) - 1 - num

    def get_epsilon_rate(self):
        if self.gamma_rate == 0:
            self.get_gamma_rate()
        return self.get_inverse(self.gamma_rate, self.digits)

    def part1(self):
        gamma_rate = self.get_gamma_rate()
        epsilon_rate = self.get_epsilon_rate()

        return gamma_rate * epsilon_rate

    def get_o2_generator_rating(self):
        return self._get_rating(1)

    def get_co2_scrubber_rating(self):
        self.co2_scrubber_rating = self._get_rating(0)
        return self.co2_scrubber_rating

    def _get_rating(self, tie_breaker_number: int):
        if tie_breaker_number != 0 and tie_breaker_number != 1:
            raise RuntimeError('Tie breaker number must be either 1 or 0')

        input_copy = self.input.copy()

        for place in range(self.digits).__reversed__():
            if len(input_copy) == 1:
                return input_copy[0]
            ones_list = []
            zeroes_list = []
            for number in input_copy:
                if self.get_whether_one_place(number, place):
                    ones_list.append(number)
                else:
                    zeroes_list.append(number)
            diff = len(ones_list) - len(zeroes_list)
            if diff > 0:                      # more ones
                if tie_breaker_number == 0:
                    remove_list = ones_list
                else:
                    remove_list = zeroes_list
            elif diff < 0:                    # more zeroes
                if tie_breaker_number == 0:
                    remove_list = zeroes_list
                else:
                    remove_list = ones_list
            else:                             # even split
                if tie_breaker_number == 0:
                    remove_list = ones_list
                else:
                    remove_list = zeroes_list
            for number in remove_list:
                input_copy.remove(number)

        if len(input_copy) != 1:
            raise RuntimeError(f'Input list was NOT narrowed down to one element, input copy: {input_copy}')
        return input_copy[0]

    def part2(self):
        """
        Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator
        rating by the CO2 scrubber rating.
        """
        # get count of 1s and 0s
        # O2 generator: more numerous or 1 if equal
        # CO2 scrubber: less numerous or 0 if equal
        o2_rating = self.get_o2_generator_rating()
        co2_rating = self.get_co2_scrubber_rating()
        return o2_rating * co2_rating
