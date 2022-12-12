
import unittest
from src.part12 import part_one, part_one_bfs,  part_two, part_two_bfs, read_input
import numpy as np

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.filename = "../resources/part12_test.txt"

    def test_part1(self):

        content = read_input(self.filename)
        self.assertEqual(31, part_one(content))
        self.assertEqual(31, part_one_bfs(content))# add assertion here

    def test_part2(self):

        content = read_input(self.filename)
        self.assertEqual(29, part_two(content))  # add assertion here
        self.assertEqual(29, part_two_bfs(content))

if __name__ == '__main__':
    unittest.main()
