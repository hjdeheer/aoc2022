import collections
import copy
from collections import deque

import numpy as np
def read_input(filename: str):
    instructions = []
    with open(filename, 'r') as file:
        for line in file:
            instruction = line.strip().split(" ")
            instructions.append((instruction[0], int(instruction[1])))
    return instructions

#If tail is in range we return True
def in_range(head, tail):
    diffX = abs(head[0] - tail[0])
    diffY = abs(head[1] - tail[1])
    return diffX < 2 and diffY < 2


def visualize_tail(visited, part):
    visited = list(set(visited))
    # Fix out of bounds
    i = min(visited, key=lambda x: x[0])[0]
    j = min(visited, key=lambda x: x[1])[1]
    offset_i = -i if i < 0 else 0
    offset_j = -j if j < 0 else 0
    visited = [(x + offset_i, y + offset_j) for (x, y) in visited]

    # Create show array
    i = max(visited, key=lambda x: x[0])[0]
    j = max(visited, key=lambda x: x[1])[1]

    show = np.empty((i + 1, j + 1), dtype=object)
    show[show == None] = '.'
    for el in visited:
        row = i - el[0]
        column = el[1]
        show[row][column] = '#'
    # Save message
    np.savetxt(f'../messages/message{part}.txt', X=show, fmt='%s')


def adjust(head, tail):
    diffX = head[0] - tail[0]
    diffY = head[1] - tail[1]
    tail_i = tail[0]
    tail_j = tail[1]

    # Right
    if diffX == 0 and diffY == 2:
        tail_j += 1
    # Left
    elif diffX == 0 and diffY == -2:
        tail_j -= 1
    # Up
    elif diffX == 2 and diffY == 0:
        tail_i += 1
    # DOwn
    elif diffX == -2 and diffY == 0:
        tail_i -= 1
    # Diagonal cases - right top
    elif diffX >= 1 and diffY >= 1:
        tail_i += 1
        tail_j += 1
    # Top left
    elif diffX >= 1 and diffY <= -1:
        tail_i += 1
        tail_j -= 1
    # Down left
    elif diffX <= -1 and diffY <= -1:
        tail_i -= 1
        tail_j -= 1
    # Down right
    elif diffX <= -1 and diffY >= 1:
        tail_i -= 1
        tail_j += 1
    tail = (tail_i, tail_j)
    return tail


def part_one(content):
    dir_map = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1,0)}
    head = (0, 0)
    tail = (0, 0)
    visited = []
    total_v = 0
    for d, steps in content:
        direc = dir_map[d]
        for step in range(steps):
            total_v += 1
            head_i = head[0] + direc[0]
            head_j = head[1] + direc[1]
            head = (head_i, head_j)
            if in_range(head, tail):
                visited.append(tail)
                continue
            #One left of head
            tail = adjust(head, tail)
            visited.append(tail)

    visualize_tail(visited, 0)
    return len(set(visited))

def part_two(content):
    dir_map = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1,0)}
    head = (0, 0)
    visited = []
    positions = {0: (0,0), 1: (0, 0), 2: (0, 0), 3: (0, 0), 4: (0, 0), 5: (0, 0), 6: (0, 0), 7: (0, 0), 8: (0, 0), 9: (0, 0)}

    for d, steps in content:
        direc = dir_map[d]
        for step in range(steps):
            begin = positions[0]
            begin_i = begin[0] + direc[0]
            begin_j = begin[1] + direc[1]
            positions[0] = (begin_i, begin_j)
            for rope in range(1, len(positions.keys())):
                head = positions[rope - 1]
                tail = positions[rope]
                if in_range(head, tail):
                    if rope == 9:
                        visited.append(tail)
                    continue
                updated_tail = adjust(head, tail)
                #Update pos of follower
                positions[rope] = updated_tail
                if rope == 9:
                    visited.append(updated_tail)

    visualize_tail(visited, 1)
    return len(set(visited))


if __name__ == "__main__":
    filename = "../resources/part9.txt"
    content = read_input(filename)
    score = part_one(content)
    score2 = part_two(content)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")

