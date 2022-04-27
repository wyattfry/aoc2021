import sys
from typing import List, Dict
from aoc2021.solutionbase import SolutionBase


class Day08(SolutionBase):
    """
    --- Day 8: Seven Segment Search ---
    """
    DAY: int = 8

    segment_to_digit_dict = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9
    }

    def __init__(self, puzzle_input: List[str]):
        self.puzzle_input = puzzle_input
        """
        [10 digit signal pattern] | [4 digit output]
        """

    @staticmethod
    def is_unique_length(segment_string: str) -> bool:
        unique_segment_lengths = [2, 4, 3, 7]
        return len(segment_string) in unique_segment_lengths

    @staticmethod
    def count_unique_lengths(segments: str) -> int:
        count = 0
        for digit in segments.split(' '):
            count += 1 if Day08.is_unique_length(digit) else 0
        return count

    def count_unique_lengths_in_all_digit_outputs(self) -> int:
        count = 0
        for signal_output in self.puzzle_input:
            [signal, output] = signal_output.split(' | ')
            count += Day08.count_unique_lengths(output)
        return count

    @staticmethod
    def get_descramble_dict(entry: str) -> Dict[str, str]:
        """
        entry: "<SIGNAL> | <DIGITS>"
        e.g. "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
        """
        descramble_dict = {x: "" for x in "abcdefg"}
        # descramble_dict:
        #   key:   scrambled
        #   value: de-scrambled
        [signal, _] = entry.split(" | ")
        counts = {x: 0 for x in "abcdefg "}
        for x in signal:
            counts[x] += 1

        # Step 1: the unique count segments: b (6), e (4)
        scrambled_b = ""
        scrambled_e = ""
        for k in counts:
            if counts[k] == 6:
                descramble_dict[k] = "b"
                scrambled_b = k
            if counts[k] == 4:
                descramble_dict[k] = "e"
                scrambled_e = k

        # Step 2: difference segment in the len 3 (7) and NOT in len 2 (1) is segment 'a'
        one = ""
        seven = ""
        four = ""  # for step 5
        for segments in signal.split(" "):
            if len(segments) == 2:
                one = segments
            if len(segments) == 3:
                seven = segments
            if len(segments) == 4: # for step 5
                four = segments
        scrambled_a = set(one).symmetric_difference(set(seven)).pop()
        descramble_dict[scrambled_a] = "a"

        # Step 3: 'c' and 'a' appear 8 times, and we know 'a', so we can find 'c'
        scrambled_c = ""
        for scrambled_letter in counts:
            count = counts[scrambled_letter]
            if count == 8 and scrambled_letter != scrambled_a:
                descramble_dict[scrambled_letter] = "c"
                scrambled_c = scrambled_letter

        # Step 4: len 2 (1) is 'cf', we know 'c' so the other is 'f'
        scrambled_f = set(one).symmetric_difference({scrambled_c}).pop()
        descramble_dict[scrambled_f] = "f"

        # Step 5: len 4 (4), already know bc_f, leftover is 'd'
        scrambled_bcf = {scrambled_b, scrambled_c, scrambled_f}
        scrambled_d = set(four).symmetric_difference(scrambled_bcf).pop()
        descramble_dict[scrambled_d] = "d"

        # Step 6: last letter standing descrambles to 'g'
        scrambled_abcdef = {
            scrambled_a,
            scrambled_b,
            scrambled_c,
            scrambled_d,
            scrambled_e,
            scrambled_f
        }
        scrambled_g = set(scrambled_abcdef).symmetric_difference("abcdefg").pop()
        descramble_dict[scrambled_g] = "g"

        return descramble_dict

    @staticmethod
    def descramble_number(descramble_dict: Dict[str, str], scrambled: str) -> int:
        """ f("eg") -> 1 """
        descrambled = [x for x in "".join([descramble_dict[x] for x in scrambled])]
        descrambled.sort()
        descrambled = "".join(descrambled)
        try:
            return Day08.segment_to_digit_dict[descrambled]
        except KeyError:
            print(f"'{scrambled}' decoded to invalid pattern: '{descrambled}'")
            # sys.exit(-1)
            return -1

    @staticmethod
    def get_output_value_from_entry(entry: str) -> int:
        # entry: "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
        descramble_dict = Day08.get_descramble_dict(entry)
        [_, scrambled_output_value] = entry.split(" | ")
        output_value = 0
        i = 3
        for scrambled_digit in scrambled_output_value.split(" "):
            descrambled_digit = Day08.descramble_number(descramble_dict, scrambled_digit)
            output_value += descrambled_digit * (10 ** i)
            i -= 1
        return output_value

    def part1(self):
        """
        In the output values, how many times do digits 1, 4, 7, or 8 appear?
        digit   element count
        1       2
        4       4
        7       3
        8       7
        """
        return self.count_unique_lengths_in_all_digit_outputs()

    def part2(self):
        sum_of_output_values = 0
        for entry in self.puzzle_input:
            sum_of_output_values += Day08.get_output_value_from_entry(entry)
        return sum_of_output_values
