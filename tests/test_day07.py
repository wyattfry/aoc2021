from aoc2021.day07 import Day07
from matplotlib import pyplot as plt
from tests.file_reading_test_base import FileReadingTestBase


class TestDay07(FileReadingTestBase):
    def get_day(self):
        return "07"

    def test_setup(self):
        sut = Day07(self.input)
        sut.setup()
        expect = {
            16: 1,
            1: 2,
            2: 3,
            0: 1,
            4: 1,
            7: 1,
            14: 1
        }
        self.assertEqual(sut.crabs_at_position, expect)

    def test_get_fuel_to_position(self):
        sut = Day07(self.input)
        sut.setup()
        x = []
        y = []
        for i in range(0, 5):
            x.append(i)
            y.append(sut.get_fuel_to_position(current_position=2, crabs_at_position=2, target_position=i))
        plt.plot(x, y)
        # plt.show()
        self.assertTrue(True)

    def test_add_up_fuel_multiple_positions(self):
        sut = Day07(self.input)
        sut.setup()
        min = 0
        max = 16
        fuel_sums = [0 for _ in range(min, max)]
        for pos in sut.crabs_at_position.keys():
            x = []
            y = []
            for target_position in range(min, max):
                crabs_at_position = sut.crabs_at_position[pos]
                fuel = sut.get_fuel_to_position(pos, crabs_at_position, target_position)
                x.append(target_position)
                y.append(fuel)
                fuel_sums[target_position] += fuel
            plt.plot(x, y)
        plt.plot(x, fuel_sums)
        plt.grid()
        plt.show()
        fuel_sums.sort()
        result = fuel_sums[0]
        self.assertEqual(result, 37)

    def test_get_total_fuel_all_crabs_to_position(self):
        sut = Day07(self.input)
        sut.setup()
        fuel_sums = sut.get_total_fuel_all_crabs_to_position()
        result = min(fuel_sums)
        self.assertEqual(result, 37)

    def test_get_fuel_to_position_corrected(self):
        sut = Day07(self.input)
        result = sut.get_fuel_to_position(0, 1, 3, corrected_calculation=True)
        self.assertEqual(result, 6)
        result = sut.get_fuel_to_position(0, 2, 3, corrected_calculation=True)
        self.assertEqual(result, 12)

    def test_part1(self):
        sut = Day07(self.input)
        res = sut.part1()
        self.assertEqual(res, 37)

    def test_part2(self):
        sut = Day07(self.input)
        res = sut.part2()
        self.assertEqual(res, 168)
