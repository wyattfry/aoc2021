from unittest import TestCase
from aoc2021.day02 import Day02


class TestDay02(TestCase):
    def test_part1_1(self):
        test_input = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
        ]
        """
        After following these instructions, you would have a horizontal position of 15 and a depth of 10.
        (Multiplying these together produces 150.)
        """
        sut = Day02(test_input)
        res = sut.part1()
        self.assertEquals(res, 150)

    def test_part2_1(self):
        test_input = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
        ]
        """
        After following these new instructions, you would have a horizontal position of 15 and a depth of 60.
        (Multiplying these produces 900.)

        """
        sut = Day02(test_input)
        res = sut.part2()
        expect = 900
        self.assertEquals(res, 900)
