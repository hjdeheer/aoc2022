import operator
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

    #Fill show array with inverted i
    show = np.empty((i + 1, j + 1), dtype=object)
    show[show == None] = '.'
    for el in visited:
        row = i - el[0]
        column = el[1]
        show[row][column] = '#'
    # Save message
    np.savetxt(f'../messages/message9_{part}.txt', X=show, fmt='%s')


def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0


def adjust(head, tail):
    diff = tuple(map(operator.sub, head, tail))
    return tail[0] + sign(diff[0]), tail[1] + sign(diff[1])

def part_one(content):
    dir_map = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1,0)}
    head = (0, 0)
    tail = (0, 0)
    visited = [tail]
    for d, steps in content:
        direc = dir_map[d]
        for step in range(steps):
            head_i = head[0] + direc[0]
            head_j = head[1] + direc[1]
            head = (head_i, head_j)
            if in_range(head, tail):
                visited.append(tail)
                continue
            tail = adjust(head, tail)
            visited.append(tail)
    visualize_tail(visited, 0)
    return len(set(visited))

def part_two(content):
    dir_map = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}
    visited = [(0, 0)]
    positions = [(0, 0)] * 10
    for d, steps in content:
        direc = dir_map[d]
        for step in range(steps):
            begin = positions[0]
            begin_i = begin[0] + direc[0]
            begin_j = begin[1] + direc[1]
            positions[0] = (begin_i, begin_j)
            for rope in range(1, len(positions)):
                head = positions[rope - 1]
                tail = positions[rope]
                if in_range(head, tail):
                    continue
                updated_tail = adjust(head, tail)
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

