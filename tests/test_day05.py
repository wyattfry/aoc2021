from aoc2021.day05 import Day05
from tests.file_reading_test_base import FileReadingTestBase


class TestDay05(FileReadingTestBase):
    def get_day(self):
        return "05"

    def test_set_or_increment_value_at_point(self):
        sut = Day05(self.input)
        sut.set_or_increment_value_at_point(0, 0)
        self.assertEqual(sut.vent_field.get(0).get(0), 1)
        sut.set_or_increment_value_at_point(0, 0)
        self.assertEqual(sut.vent_field.get(0).get(0), 2)

    def test_inclusive_range(self):
        sut = Day05(self.input)
        result = sut.inclusive_range(0, 3)
        self.assertEqual(result, [0, 1, 2, 3])
        result = sut.inclusive_range(3, 0)
        self.assertEqual(result, [3, 2, 1, 0])

    def test_part1(self):
        sut = Day05(self.input)
        res = sut.part1()
        self.assertEquals(res, 5)

    def test_part2(self):
        sut = Day05(self.input)
        res = sut.part2()
        self.assertEquals(res, 12)
