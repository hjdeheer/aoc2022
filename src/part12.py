import collections
import sys
from queue import PriorityQueue
import operator
import time


def read_input(filename: str):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            row = [x for x in line.strip()]
            grid.append(row)
    return grid



def get_height(row, column, grid):
    return grid[row][column]
def get_neigbours(node, grid):
    dir_map = {'left': (0, -1), 'right':(0, 1), 'up': (-1, 0), 'down': (1, 0)}
    neighbours = []
    for dir in dir_map.values():
        height = get_height(*node, grid)
        if height == 'S':
            height = 'a'
        elif height == 'E':
            height = 'z'

        new_pos = tuple(map(operator.add, node, dir))
        #If in bounds
        if 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]):
            new_height = get_height(*new_pos, grid)
            if new_height == 'S':
                new_height = 'a'
            elif new_height == 'E':
                new_height = 'z'
            if ord(new_height) - ord(height) <= 1:
                neighbours.append(new_pos)
    return neighbours






def dijkstra(S, E, grid, part2=None):
    end = (0, 0)
    visited = set()
    distances = collections.defaultdict(int)
    Q = PriorityQueue()

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == S or (part2 and grid[row][column] == 'a'):
                Q.put((0, row, column))
                visited.add((row, column))
                distances[(row, column)] = 0
            else:
                distances[(row, column)] = sys.maxsize

            if grid[row][column] == E:
                end = (row, column)
                distances[(row, column)] = sys.maxsize

    while not Q.empty():
        d, row, column = Q.get()
        neighbours = get_neigbours((row, column), grid)
        for neighbour in neighbours:
            curr_d = d + 1
            distances[neighbour] = min(curr_d, distances[neighbour])
            if neighbour not in visited:
                visited.add(neighbour)
                Q.put((distances[neighbour], neighbour[0], neighbour[1]))
    return distances[end]

def bfs(S, E, grid,part2=None):
    visited = set()
    Q = collections.deque()

    #We can start an any elevation of 'a'
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == S or part2 and grid[row][column] == 'a':
                Q.append(((row, column), 0))
                visited.add((row, column))

    while not len(Q) == 0:
        node, d = Q.popleft()
        neighbours = get_neigbours(node, grid)
        for n in neighbours:
            curr_d = d + 1
            if get_height(*n, grid) == E:
                return curr_d
            if n not in visited:
                visited.add(n)
                Q.append((n, curr_d))

    return -1


def get_starting_pos(grid):
    starting_pos = []
    #Get all starting posisions and set end
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 'S' or grid[row][column] == 'a':
                starting_pos.append((row, column))
    return starting_pos



def part_one(grid: list[list[str]]):
    return dijkstra('S', 'E', grid)


def part_one_bfs(grid: list[list[str]]):
    return bfs('S', 'E', grid)

def part_two(grid: list[list[str]]):
    return dijkstra('S', 'E', grid, True)

def part_two_bfs(grid: list[list[str]]):
    return bfs('S', 'E', grid, True)



if __name__ == "__main__":
    filename = "../resources/part12.txt"
    grid = read_input(filename)

    start_time = time.time()
    score = part_one_bfs(grid)
    print(f"Part one bfs: {score} - {(time.time() - start_time):.3f}s")

    start_time = time.time()
    score = part_one(grid)
    print(f"Part one: {score} - {(time.time() - start_time):.3f}s")



    start_time = time.time()
    score = part_two_bfs(grid)
    print(f"Part two bfs: {score} - {(time.time() - start_time):.3f}s")


    start_time = time.time()
    score = part_two(grid)
    print(f"Part two: {score} - {(time.time() - start_time):.3f}s")




