
import unittest
from src.part13 import part_one, part_two, read_input, read_input_two
import numpy as np

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.filename = "../resources/part13_test.txt"

    def test_part1(self):

        content = read_input(self.filename)
        self.assertEqual(13, part_one(content))

    def test_part2(self):

        content = read_input_two(self.filename)
        self.assertEqual(140, part_two(content))  # add assertion here


if __name__ == '__main__':
    unittest.main()
