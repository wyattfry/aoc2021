#!/usr/bin/env bash
set -e

two_digit_day="${1}" # e.g. 04, 12

function make_input_file() {
  touch "./aoc2021/input_files/input${two_digit_day}.txt"
}
function make_test_script() {
  cat <<- HEREDOC > "./tests/test_day${two_digit_day}.py"
from unittest import TestCase
from aoc2021.dayTWO_DIGIT_DAY import DayTWO_DIGIT_DAY


class TestDayTWO_DIGIT_DAY(TestCase):
  def __init__(self):
      self.input = [x.strip() for x in open("./input_files/inputTWO_DIGIT_DAY.txt").readlines()]

  def test_part1(self):
      sut = DayTWO_DIGIT_DAY(self.input)
      res = sut.part1()
      self.assertEquals(res, 1)

  def test_part2(self):
      sut = DayTWO_DIGIT_DAY(self.input)
      res = sut.part2()
      self.assertEquals(res, 1)

HEREDOC

  sed -i '' "s/TWO_DIGIT_DAY/${two_digit_day}/g" "./tests/test_day${two_digit_day}.py"
  black "./tests/test_day${two_digit_day}.py"
}

function make_solution_script() {
  cat <<- HEREDOC > "./aoc2021/day${two_digit_day}.py"
from aoc2021.solution import Solution


class DayTWO_DIGIT_DAY(Solution):
    day: int = -1

    def __init__(self, puzzle_input):
        self.input = puzzle_input

    def part1(self) :
        return 0

    def part2(self):
        return 0
HEREDOC

  sed -i '' "s/TWO_DIGIT_DAY/${two_digit_day}/g" "./aoc2021/day${two_digit_day}.py"
  black "./aoc2021/day${two_digit_day}.py"
}

function make_test_input_file() {
  touch "./tests/input_files/input${two_digit_day}.txt"
}


make_input_file
make_test_script
make_solution_script
make_test_input_file
