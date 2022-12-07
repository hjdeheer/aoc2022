import collections
import copy
from collections import deque

def read_input(filename: str):
    with open(filename, 'r') as file:
        return file.read().strip()


def part_one(content):
    for i in range(4, len(content)):
        substring = content[i-4:i]
        duplicate = {c for c in substring}
        if len(duplicate) == 4:
            return i
    return -1


def part_two(content):
    for i in range(14, len(content)):
        substring = content[i-14:i]
        duplicate = {c for c in substring}
        if len(duplicate) == 14:
            return i
    return -1


if __name__ == "__main__":
    filename = "../resources/part6.txt"
    content = read_input(filename)
    score = part_one(content)
    score2 = part_two(content)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")

