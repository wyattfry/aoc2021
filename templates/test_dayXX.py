from aoc2021.dayXX import DayXX
from tests.file_reading_test_base import FileReadingTestBase


class TestDayXX(FileReadingTestBase):
    def get_day(self):
        return "XX"

    def test_part1(self):
        sut = DayXX(self.input)
        res = sut.part1()
        self.assertEquals(res, -1)

    def test_part2(self):
        sut = DayXX(self.input)
        res = sut.part2()
        self.assertEquals(res, -1)
