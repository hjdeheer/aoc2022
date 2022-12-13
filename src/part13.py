import collections
import re
import sys
from queue import PriorityQueue
import operator
import time


def read_input(filename: str):
    packets = []
    with open(filename, 'r') as file:
        pairs = file.read().strip().split('\n\n')
    for pair in pairs:
        pair = pair.split('\n')
        x = eval(pair[0])
        y = eval(pair[1])
        packets.append((x, y))
    return packets

def read_input_two(filename: str):
    packets = []
    with open(filename, 'r') as file:
        pairs = file.read().strip().split('\n\n')
    for pair in pairs:
        pair = pair.split('\n')
        x = eval(pair[0])
        y = eval(pair[1])
        packets.append(x)
        packets.append(y)
    return packets

"""
Recursive function that compares pairs.
Returns 1 if in right order and -1 if not in right order

"""
def compare(x, y):
    if type(x) == int and type(y) == int:
        if x < y:
            return 1
        elif x > y:
            return -1
        else:
            return 0
    elif type(x) == list and type(y) == list:
        i = 0
        while i < len(x) and i < len(y):
            comparison = compare(x[i], y[i])
            if comparison == -1:
                return -1
            if comparison == 1:
                return 1
            i += 1
        if len(x) < len(y):
            return 1
        elif len(x) > len(y):
            return -1
    elif type(x) == int and type(y) == list:
        return compare([x], y)
    else:
        return compare(x, [y])


def part_one(packets: list[tuple]):
    total_sum = 0
    for i, (x, y) in enumerate(packets):
        if compare(x, y) == 1:
            total_sum += i + 1
    return total_sum


def part_two(packets: list[list]):
    divider_one = [[2]]
    divider_two = [[6]]
    one = 1
    two = 2
    for i, x in enumerate(packets):
        if compare(x, divider_one) == 1:
            one += 1
        if compare(x, divider_two) == 1:
            two += 1
    return one * two

if __name__ == "__main__":
    filename = "../resources/part13.txt"
    packets = read_input(filename)

    start_time = time.time()
    score = part_one(packets)
    print(f"Part one: {score} - {(time.time() - start_time):.3f}s")

    packets_two = read_input_two(filename)
    start_time = time.time()
    score = part_two(packets_two)
    print(f"Part two: {score} - {(time.time() - start_time):.3f}s")




