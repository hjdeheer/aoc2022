
import unittest
from src.part14 import part_one, part_two, read_input
import numpy as np

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.filename = "../resources/part14_test.txt"

    def test_part1(self):

        content, r, c = read_input(self.filename)
        self.assertEqual(24, part_one(content, r, c))

    def test_part2(self):

        content, r, c = read_input(self.filename)
        self.assertEqual(93, part_two(content, r, c))  # add assertion here


if __name__ == '__main__':
    unittest.main()
