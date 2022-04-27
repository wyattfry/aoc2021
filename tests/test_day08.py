from unittest import skip, TestCase

from aoc2021.day08 import Day08
from tests.file_reading_test_base import FileReadingTestBase


class TestDay08(FileReadingTestBase):
    def get_day(self):
        return "08"

    def test_is_unique_length(self):
        sut = Day08(self.input)
        result = sut.is_unique_length('aa')
        self.assertTrue(result)
        result = sut.is_unique_length('aaa')
        self.assertTrue(result)
        result = sut.is_unique_length('aaaa')
        self.assertTrue(result)
        result = sut.is_unique_length('aaaaaaa')
        self.assertTrue(result)

        result = sut.is_unique_length('aaaaa')
        self.assertFalse(result)
        result = sut.is_unique_length('aaaaaa')
        self.assertFalse(result)

    def test_count_unique_lengths(self):
        sut = Day08(self.input)
        result = sut.count_unique_lengths('aaaaa aaaaa aa')
        self.assertEqual(result, 1)

    def test_get_descramble_dict_2(self):
        test_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
        descramble_dict = Day08.get_descramble_dict(test_input)
        self.assertEqual(descramble_dict["d"], "a")
        self.assertEqual(descramble_dict["e"], "b")
        self.assertEqual(descramble_dict["a"], "c")
        self.assertEqual(descramble_dict["f"], "d")
        self.assertEqual(descramble_dict["g"], "e")
        self.assertEqual(descramble_dict["b"], "f")
        self.assertEqual(descramble_dict["c"], "g")

    def test_descramble_number(self):
        sut = Day08(self.input)
        test_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
        dd = sut.get_descramble_dict(test_input)
        expect_dict = {
            "acedgfb": 8,
            "cdfbe": 5,
            "gcdfa": 2,
            "fbcad": 3,
            "dab": 7,
            "cefabd": 9,
            "cdfgeb": 6,
            "eafb": 4,
            "cagedb": 0,
            "ab": 1
        }
        for scrambled in expect_dict:
            expect = expect_dict[scrambled]
            result = Day08.descramble_number(dd, scrambled)
            self.assertEqual(result, expect)

    def test_get_output_value_from_entry(self):
        test_entry = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
        result = Day08("").get_output_value_from_entry(test_entry)
        expect = 5353
        self.assertEqual(result, expect)

    def test_part1(self):
        sut = Day08(self.input)
        res = sut.part1()
        self.assertEqual(res, 26)

    def test_part2(self):
        sut = Day08(self.input)
        res = sut.part2()
        self.assertEqual(res, 61229)
