
import unittest
from src.part11 import part_one, part_two, read_input
import numpy as np

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.filename = "../resources/part11_test.txt"

    def test_part1(self):

        content = read_input(self.filename)
        self.assertEqual(10605, part_one(content))  # add assertion here

    def test_part2(self):

        content = read_input(self.filename)
        self.assertEqual(2713310158, part_two(content))  # add assertion here

if __name__ == '__main__':
    unittest.main()
