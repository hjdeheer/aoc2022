import unittest
from src.part9 import part_one, part_two, read_input


class MyTestCase(unittest.TestCase):

    def test_part1(self):
        filename = "../resources/part9_test.txt"
        content = read_input(filename)
        self.assertEqual(13, part_one(content))  # add assertion here

    def test_part2(self):
        filename = "../resources/part9_test2.txt"
        content = read_input(filename)

        self.assertEqual(36, part_two(content))

if __name__ == '__main__':
    unittest.main()
