import unittest
from src.part10 import part_one, part_two, read_input
import numpy as np

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.filename = "../resources/part10_test.txt"

    def test_part1(self):

        content = read_input(self.filename)
        self.assertEqual(13140, part_one(content))  # add assertion here

    def test_part2(self):

        content = read_input(self.filename)
        two = part_two(content)
        np.savetxt(f'../messages/message_10_test.txt', X=two, fmt='%s')

if __name__ == '__main__':
    unittest.main()
