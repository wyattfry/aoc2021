from unittest import TestCase
from aoc2021.day03 import Day03


class TestDay03(TestCase):
    def test_part1(self):
        test_input = [
            '1',
            '2',
            '3',
            '4'
        ]
        sut = Day03(test_input)
        res = sut.part1()
        self.assertEquals(res, 1)

    def test_part1(self):
        test_input = [
            '1',
            '2',
            '3',
            '4'
        ]
        sut = Day03(test_input)
        res = sut.part1()
        self.assertEquals(res, 1)

