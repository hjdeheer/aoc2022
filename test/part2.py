import unittest
from src.part2 import part_one, part_two, read_input

class MyTestCase(unittest.TestCase):

    def test_part1(self):
        filename = "../resources/part2_test.txt"
        games = read_input(filename)

        self.assertEqual(15, part_one(games))  # add assertion here

    def test_part2(self):
        filename = "../resources/part2_test.txt"
        games = read_input(filename)

        self.assertEqual(12, part_two(games))

if __name__ == '__main__':
    unittest.main()
