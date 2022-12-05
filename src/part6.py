import collections
import copy
from collections import deque

def read_input(filename: str):
    map = collections.defaultdict(deque)
    with open(filename, 'r') as file:
        content = file.read().split('\n\n')
    return


def part_one(conten):
    return

def part_two(content):
    return


if __name__ == "__main__":
    filename = "../resources/part6.txt"
    content = read_input(filename)
    score = part_one(content)
    score2 = part_two(content)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")

