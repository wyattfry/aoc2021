from unittest import TestCase
from aoc2021.day01 import Day01


class TestDay01(TestCase):
    def test_part2(self):
        test_input = ['1', '2', '3', '4']
        sut = Day01(test_input)
        res = sut.part2()
        self.assertIs(res, 1)

    def test_part2_2(self):
        test_input = [
            '199',
            '200',
            '208',
            '210',
            '200',
            '207',
            '240',
            '269',
            '260',
            '263'
        ]
        sut = Day01(test_input)
        res = sut.part2()
        self.assertIs(res, 5)
