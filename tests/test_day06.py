from aoc2021.day06 import Day06
from tests.file_reading_test_base import FileReadingTestBase


class TestDay06(FileReadingTestBase):
    def get_day(self):
        return "06"

    def test_get_school_size(self):
        sut = Day06(self.input)
        sut.lanternfish_school = {
            0: 1,
            1: 2,
            2: 4
        }
        self.assertEqual(sut.get_school_size(), 7)

    def test_parse_puzzle_input(self):
        sut = Day06(self.input)
        sut.setup()
        expect = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 1,
            5: 0,
            6: 0,
            7: 0,
            8: 0
        }
        self.assertEqual(sut.lanternfish_school, expect)

    def test_simulate_fish_day(self):
        sut = Day06(self.input)
        sut.setup()
        expect = {
            0: 1,
            1: 1,
            2: 2,
            3: 1,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0
        }
        sut.simulate_fish_day()
        self.assertEqual(sut.lanternfish_school, expect)
        sut.simulate_fish_day()
        expect = {
            0: 1,
            1: 2,
            2: 1,
            3: 0,
            4: 0,
            5: 0,
            6: 1,
            7: 0,
            8: 1
        }
        self.assertEqual(sut.lanternfish_school, expect)

    def test_part1(self):
        """
        In this example, after 18 days, there are a total of 26 fish.
        After 80 days, there would be a total of 5934.
        """
        sut = Day06(self.input)
        res = sut.part1()
        self.assertEquals(res, 5934)

    def test_part2(self):
        sut = Day06(self.input)
        res = sut.part2()
        self.assertEquals(res, 26984457539)
