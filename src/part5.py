import collections
import copy
from collections import deque

def read_input(filename: str):
    map = collections.defaultdict(deque)
    with open(filename, 'r') as file:
        content = file.read().split('\n\n')
    rows = content[0].splitlines()[::-1]
    stacks = [int(x) for x in rows[0].split("  ")]
    for row in rows[1:]:
        index = 1
        for stack in stacks:
            element = row[index:index + 1].strip()
            if element != '':
                map[stack].append(element)
            index += 4

    instructions = []
    for instruction in content[1].splitlines():
        inst = instruction.split(' ')
        instructions.append((int(inst[1]), int(inst[3]), int(inst[5])))

    return map, instructions


def part_one(content, instructions):
    for instruction in instructions:
        n = instruction[0]
        from_stack = instruction[1]
        to_stack = instruction[2]
        for el in range(0, n):
            to_move = content[from_stack].pop()
            content[to_stack].append(to_move)
    return "".join([value[-1] for value in content.values()])

def part_two(content, instructions):
    for instruction in instructions:
        n = instruction[0]
        from_stack = instruction[1]
        to_stack = instruction[2]
        if n == 1:
            to_move = content[from_stack].pop()
            content[to_stack].append(to_move)
        else:
            moving_arr = []
            for el in range(0, n):
                moving_arr.append(content[from_stack].pop())
            for el in moving_arr[::-1]:
                content[to_stack].append(el)
    return "".join([value[-1] for value in content.values()])

if __name__ == "__main__":
    filename = "../resources/part5.txt"
    map, instructions = read_input(filename)
    score = part_one(copy.deepcopy(map), copy.deepcopy(instructions))
    score2 = part_two(map, instructions)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")

