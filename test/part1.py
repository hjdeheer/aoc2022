import unittest
from src.part1 import part_one, part_two, read_input

class MyTestCase(unittest.TestCase):

    def test_part1(self):
        filename = "../resources/part1_test.txt"
        elves = read_input(filename)

        self.assertEqual(24000, part_one(elves))  # add assertion here

    def test_part2(self):
        filename = "../resources/part1_test.txt"
        elves = read_input(filename)

        self.assertEqual(part_two(elves), 45000)

if __name__ == '__main__':
    unittest.main()
