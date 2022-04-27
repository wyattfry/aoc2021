from aoc2021.day03 import Day03
from tests.file_reading_test_base import FileReadingTestBase


class TestDay03(FileReadingTestBase):

    def get_day(self) -> str:
        return "03"

    def test_parse_00100_b2_to_4_b10(self):
        sut = Day03(self.input)
        res = sut.input
        self.assertEqual(res[0], 4)

    def test_get_whether_one_place(self):
        cases = [
            (Day03.get_whether_one_place(12, 0), False),
            (Day03.get_whether_one_place(12, 1), False),
            (Day03.get_whether_one_place(12, 2), True),
            (Day03.get_whether_one_place(12, 3), True),
            (Day03.get_whether_one_place(12, 4), False),
        ]
        i = 0
        for case in cases:
            with self.subTest(i=i):
                self.assertEqual(case[0], case[1])
                i += 1

    def test_get_whether_more_ones(self):
        self.assertTrue(Day03.get_whether_more_ones([1]))
        self.assertTrue(Day03.get_whether_more_ones([1,0,1]))

        self.assertFalse(Day03.get_whether_more_ones([0]))
        self.assertFalse(Day03.get_whether_more_ones([1,0,1,0]))

    def test_get_gamma_rate(self):
        sut = Day03(self.input)
        gamma_rate = sut.get_gamma_rate()
        expect = 22
        self.assertEqual(gamma_rate, expect)

    def test_get_o2_generator_rating(self):
        sut = Day03(self.input)
        """the oxygen generator rating is 10111, or 23 in decimal."""
        self.assertEqual(sut.get_o2_generator_rating(), 23)

    def test_get_co2_scrubber_rating(self):
        sut = Day03(self.input)
        """the oxygen generator rating is 10111, or 23 in decimal."""
        self.assertEqual(sut.get_co2_scrubber_rating(), 10)

    def test_part2(self):
        sut = Day03(self.input)
        """the oxygen generator rating is 10111, or 23 in decimal."""
        self.assertEqual(sut.part2(), 230)



