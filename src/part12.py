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

def get_neigbours(node, grid):
    dir_map = {'left': (0, -1), 'right':(0, 1), 'up': (-1, 0), 'down': (1, 0)}
    neighbours = []
    for dir in dir_map.values():
        if grid[node[0]][node[1]] == 'S':
            height = 'a'
        elif grid[node[0]][node[1]] == 'E':
            height = 'z'
        else:
            height = grid[node[0]][node[1]]
        new_pos = tuple(map(operator.add, node, dir))

        #If in bounds
        if 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]):
            new_height = grid[new_pos[0]][new_pos[1]]
            if grid[new_pos[0]][new_pos[1]] == 'S':
                new_height = 'a'
            elif grid[new_pos[0]][new_pos[1]] == 'E':
                new_height = 'z'
            if ord(new_height) - ord(height) <= 1:
                neighbours.append(new_pos)
    return neighbours

def dijkstra(S, E, grid):
    end = (0, 0)
    visited = set()
    distances = collections.defaultdict(int)
    Q = PriorityQueue()

    # Add start position
    if type(S) == tuple:
        S = grid[S[0]][S[1]]

    if type(E) == tuple:
        E = grid[E[0]][E[1]]

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == S:
                Q.put((0, row, column))
            elif grid[row][column] == E:
                end = (row, column)
                distances[(row, column)] = sys.maxsize
            else:
                distances[(row, column)] = sys.maxsize

    while not Q.empty():
        node = Q.get()
        neighbours = get_neigbours((node[1], node[2]), grid)
        for neighbour in neighbours:
            curr_d = distances[(node[1], node[2])] + 1
            if curr_d < distances[neighbour]:
                distances[neighbour] = curr_d
            q_instance = (distances[neighbour], neighbour[0], neighbour[1])
            #Check for duplicates and visited
            if neighbour not in visited and not q_instance in Q.queue:
                Q.put((distances[neighbour], neighbour[0], neighbour[1]))
        visited.add((node[1], node[2]))
    return distances[end]

def bfs(S, E, grid):
    visited = set()
    Q = collections.deque()


    #Add start position
    if type(S) == tuple:
        S = grid[S[0]][S[1]]

    if type(E) == tuple:
        E = grid[E[0]][E[1]]


    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == S:
                Q.append(((row, column), 0))

    while not len(Q) == 0:
        node, d = Q.popleft()
        neighbours = get_neigbours(node, grid)
        for n in neighbours:
            curr_d = d + 1
            if grid[n[0]][n[1]] == E:
                return curr_d
            #Check for duplicates
            q_instance = (n, curr_d)
            if n not in visited and q_instance not in Q:
                Q.append((n, curr_d))
        visited.add(node)
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
    return min([dijkstra(start, 'E', grid) for start in get_starting_pos(grid)])

def part_two_bfs(grid: list[list[str]]):
    return min([bfs(start, 'E', grid) for start in get_starting_pos(grid)])


if __name__ == "__main__":
    filename = "../resources/part12.txt"
    grid = read_input(filename)
    #
    # #1 bfs
    start_time = time.time()
    score = part_one_bfs(grid)
    print(f"Part one: {score} - {(time.time() - start_time):.3f}s")

    # #1 dijkstra
    start_time = time.time()
    score = part_one(grid)
    print(f"Part one: {score} - {(time.time() - start_time):.3f}s")


    #1 dijkstra
    start_time = time.time()
    score = part_two(grid)
    print(f"Part two: {score} - {(time.time() - start_time):.3f}s")

    # 1 bfs
    start_time = time.time()
    score = part_two_bfs(grid)
    print(f"Part two: {score} - {(time.time() - start_time):.3f}s")


