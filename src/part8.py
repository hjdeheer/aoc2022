import collections
import copy
from collections import deque


def read_input(filename: str):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip()]
            grid.append(row)
    return grid


def is_visible(grid:list[list[int]], i: int, j: int):
    tree_height = grid[i][j]
    k, l = i, j
    dir_map = {'left': (0, -1), 'right':(0, 1), 'up': (-1, 0), 'down': (1, 0)}
    for direction in dir_map.keys():
        direc = dir_map[direction]
        i += direc[0]
        j += direc[1]
        direction_vis = True
        while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            height = grid[i][j]
            if height >= tree_height:
                direction_vis = False

            i += direc[0]
            j += direc[1]
        if direction_vis:
            return True
        i, j = k, l
    return False

def get_viewing_distance(grid:list[list[int]], i: int, j: int):
    tree_height = grid[i][j]
    k, l = i, j
    dir_map = {'left': (0, -1), 'right':(0, 1), 'up': (-1, 0), 'down': (1, 0)}
    view_dist = collections.defaultdict(int)
    total_view = 1
    for direction in dir_map.keys():
        view = 0
        direc = dir_map[direction]
        i += direc[0]
        j += direc[1]
        while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            curr_tree = grid[i][j]
            view += 1
            if curr_tree >= tree_height:
                break
            i += direc[0]
            j += direc[1]
        view_dist[direction] = view
        i, j = k, l
    for view in view_dist.values():
        total_view *= view
    return total_view




def part_one(grid: list[list[int]]):
    n_rows = len(grid)
    n_columns = len(grid[0])
    already_vis = n_columns + (2 * (n_rows - 1)) + n_columns - 2
    n_visible = already_vis
    for i in range(1, n_rows - 1):
        for j in range(1, n_columns - 1):
            tree_visible = is_visible(grid, i, j)
            if tree_visible:
                n_visible += 1
    return n_visible


def part_two(grid: list[list[int]]):
    n_rows = len(grid)
    n_columns = len(grid[0])
    view_range = 0
    for i in range(0, n_rows):
        for j in range(0, n_columns):
            view_range = max(view_range, get_viewing_distance(grid, i, j))
    return view_range


if __name__ == "__main__":
    filename = "../resources/part8.txt"
    grid = read_input(filename)
    score = part_one(grid)
    score2 = part_two(grid)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")
