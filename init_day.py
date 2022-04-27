#!/usr/bin/env python3
from os import path
from sys import argv, stderr
import re

if len(argv) != 2:
    print(f"Requires one argument, the day to generate, e.g. {argv[0]} 05", file=stderr)
    exit(1)
day: str = argv[1]
input_valid = bool(re.match("[0-9]{2}", day))
if not input_valid:
    print(f"Argument '{day}' is invalid. Must match the pattern `[0-9]{{2}}`", file=stderr)
    exit(2)

input_file_path = path.join("aoc2021", "input_files", f"input{day}.txt")
print(f"Creating input file      \t{input_file_path}")
open(input_file_path, "w+").write(f"PASTE DAY {day} PUZZLE INPUT HERE")

solution_template_path = path.join("templates", "dayXX.py")
filled_in = [i.replace("XX", day) for i in open(solution_template_path, "r").readlines()]
solution_path = path.join("aoc2021", f"day{day}.py")
print(f"Creating solution script \t{solution_path}")
open(solution_path, "w+").writelines(filled_in)

example_input_file_path = path.join("tests", "input_files", f"input{day}.txt")
print(f"Creating test input file \t{example_input_file_path}")
open(example_input_file_path, "w+").write(f"PASTE DAY {day} EXAMPLE PUZZLE INPUT HERE")

test_template_path = path.join("templates", "test_dayXX.py")
filled_in = [i.replace("XX", day) for i in open(test_template_path, "r").readlines()]
test_path = path.join("tests", f"test_day{day}.py")
print(f"Creating test class      \t{test_path}")
open(test_path, "w+").writelines(filled_in)

print("Done.")
