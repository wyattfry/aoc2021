from unittest import TestCase
from os import path


class FileReadingTestBase(TestCase):

    original_input = []
    input = []

    def get_day(self) -> str:
        raise NotImplementedError('Child classes must implement this method')

    def setUp(self) -> None:
        if len(self.original_input) == 0:
            input_file = path.join(path.dirname(__file__), "input_files", f"input{self.get_day()}.txt")
            with open(input_file) as file:
                self.original_input = [x.strip() for x in file.readlines()]
        self.input = self.original_input.copy()