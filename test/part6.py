import unittest
from src.part6 import part_one, part_two, read_input

class MyTestCase(unittest.TestCase):

    def test_part1(self):
        filename = "../resources/part6_test.txt"
        content, i = read_input(filename)

        self.assertEqual('CMZ', part_one(content, i))  # add assertion here

    def test_part2(self):
        filename = "../resources/part6_test.txt"
        content, i = read_input(filename)

        self.assertEqual('MCD', part_two(content, i))

if __name__ == '__main__':
    unittest.main()
