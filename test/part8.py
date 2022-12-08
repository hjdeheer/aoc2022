import unittest
from src.part8 import part_one, part_two, read_input


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.filename = "../resources/part8_test.txt"

    def test_part1(self):

        content = read_input(self.filename)
        self.assertEqual(21, part_one(content))  # add assertion here

    def test_part2(self):

        content = read_input(self.filename)

        self.assertEqual(8, part_two(content))

if __name__ == '__main__':
    unittest.main()
