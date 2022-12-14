import collections
import copy
import re
import sys
from queue import PriorityQueue
import operator
import time

import numpy as np


def read_input(filename: str):
    paths = []
    max_r, max_c = 0, 0
    with open(filename, 'r') as file:
        for path in file:
            points = path.strip().split(' -> ')
            path = []
            for point in points:
                coor = point.split(',')
                r = int(coor[1])
                c = int(coor[0])
                max_r = max(max_r, r)
                max_c = max(max_c, c)
                path.append((r, c))
            paths.append(path)
    return paths, max_r, max_c



def fill_grid(cave, path):
    for i in range(1, len(path)):
        prev = path[i-1]
        curr = path[i]
        diff_x = curr[0] - prev[0]
        diff_y = curr[1] - prev[1]
        start_x = curr[0]
        start_y = curr[1]
        #If down
        if diff_x > 0:
            for i in range(prev[0], curr[0] + 1):
                cave[i][start_y] = '#'
        #If up
        elif diff_x < 0:
            for i in range(curr[0], prev[0] + 1):
                cave[i][start_y] = '#'
        #If right
        elif diff_y > 0:
            for i in range(prev[1], curr[1] + 1):
                cave[start_x][i] = '#'
        #If left
        elif diff_y < 0:
            for i in range(curr[1], prev[1] + 1):
                cave[start_x][i]  = '#'

def falling_sand(grid):
    sand_x = 0
    sand_y = 500

    blocked = False
    while not blocked:
        #If into abyss
        if not(0 <= sand_x + 1 < len(grid) and 0 <= sand_y - 1 < len(grid[0]) and 0 <= sand_y + 1 < len(grid[0])):
            return True
        elif grid[0][500] == 'o':
            return True
        #First move down
        if grid[sand_x + 1][sand_y] == '.':
            sand_x += 1
        elif grid[sand_x + 1][sand_y - 1] == '.':
            sand_x += 1
            sand_y -= 1
        elif grid[sand_x + 1][sand_y + 1] == '.':
            sand_x += 1
            sand_y += 1
        else:
            grid[sand_x][sand_y] = 'o'
            blocked = True
    return False


def part_one(paths: list[list[tuple]], max_r, max_c):
    print(max_r, max_c)
    cave = np.empty(shape=(max_r + 1, max_c + 1), dtype=str)
    cave[cave == ''] = '.'

    for path in paths:
        fill_grid(cave, path)
    print(cave)

    sand = 0
    in_abyss = False
    while not in_abyss:
        in_abyss = falling_sand(cave)
        if not in_abyss:
            sand += 1

    np.savetxt('../messages/message13_0.txt', X=cave, fmt='%s')
    return sand



def part_two(paths: list[list[tuple]], max_r, max_c):
    cave = np.empty(shape=(max_r + 3, 1000), dtype=str)
    cave[cave == ''] = '.'
    #Add floor
    for i in range(len(cave[0])):
        floor = len(cave) - 1
        cave[floor][i] = '#'

    for path in paths:
        fill_grid(cave, path)

    sand = 0
    in_abyss = False
    while not in_abyss:
        in_abyss = falling_sand(cave)
        if not in_abyss:
            sand += 1

    np.savetxt('../messages/message13_1.txt', X=cave, fmt='%s')
    return sand


if __name__ == "__main__":
    filename = "../resources/part14.txt"
    paths, r, c = read_input(filename)

    start_time = time.time()
    score = part_one(copy.deepcopy(paths), r, c)
    print(f"Part one: {score} - {(time.time() - start_time):.3f}s")


    start_time = time.time()
    score = part_two(paths, r, c)
    print(f"Part two: {score} - {(time.time() - start_time):.3f}s")




