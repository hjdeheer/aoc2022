import collections
import copy
from collections import deque

import numpy as np
def read_input(filename: str):
    instructions = []
    with open(filename, 'r') as file:
        for line in file:
            instruction = line.strip().split(" ")
            if len(instruction) == 1:
                instructions.append(instruction[0])
            else:
                instructions.append((instruction[0], int(instruction[1])))
    return instructions


def part_one(content):
    cycles = [20, 60, 100, 140, 180, 220]
    cycle = 0
    X = 1
    total = 0
    for operation in content:
        if len(cycles) == 0:
            break
        first_cycle = cycles[0]
        #We increment the cycle ->
        if operation == 'noop':
            cycle += 1
            if cycle == first_cycle:
                total += cycles.pop(0) * X

        elif operation[0] == 'addx':
            cycle += 2
            #During cycle
            if cycle >= first_cycle:
                total += cycles.pop(0) * X
            X += operation[1]
    return total


def during_cycle(cycle, X, crt):
    if abs((cycle % 40) - X) <= 1:
        crt.append('#')
    else:
        crt.append('.')
    cycle += 1
    return cycle

def part_two(content):
    crt = []
    cycle = 0
    X = 1
    for operation in content:
        if cycle == 240:
            break
        if operation == 'noop':
            cycle = during_cycle(cycle, X, crt)
        elif operation[0] == 'addx':
            cycle = during_cycle(cycle, X, crt)
            cycle = during_cycle(cycle, X, crt)
            X += operation[1]
    crt = np.reshape(np.array(crt), (-1, 40))
    return crt


if __name__ == "__main__":
    filename = "../resources/part10.txt"
    content = read_input(filename)
    score = part_one(content)
    score2 = part_two(content)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")
    np.savetxt(f'../messages/message_10.txt', X=score2, fmt='%s')

