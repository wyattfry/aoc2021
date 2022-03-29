from unittest import TestCase
from aoc2021.day04 import Day04


class TestDay04(TestCase):
    def __init__(self):
        self.input = [x.strip() for x in open("./input_files/input04.txt").readlines()]

    def test_part1(self):
        sut = Day04(self.input)
        res = sut.part1()
        self.assertEquals(res, 1)

    def test_part2(self):
        sut = Day04(self.input)
        res = sut.part2()
        self.assertEquals(res, 1)
