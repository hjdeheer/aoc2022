import collections
import sys
from queue import PriorityQueue
import operator
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



def part_one(grid: list[list[str]]):
    E = (0, 0)
    visited = set()
    distances = collections.defaultdict(int)
    Q = PriorityQueue()
    for row in range(len(grid)):
        for column in range(len(grid[0])):

            if grid[row][column] == 'S':
                Q.put((0, row, column))
            elif grid[row][column] == 'E':
                E = (row, column)
                distances[(row, column)] = sys.maxsize
            else:
                distances[(row, column)] = sys.maxsize
    #print(distances)
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
    #print(distances)
    return distances[E]


def part_two(grid: list[list[int]]):

    starting_pos = []
    global_dist = []
    E = (0, 0)

    #Get all starting posisions and set end
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 'S' or grid[row][column] == 'a':
                starting_pos.append((row, column))
            elif grid[row][column] == 'E':
                E = (row, column)


    for s in starting_pos:
        visited = set()
        distances = collections.defaultdict(int)
        #First item in queue
        Q = PriorityQueue()
        Q.put((0, *s))
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if (row, column) != s:
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
        global_dist.append(distances[E])

    return min(global_dist)


if __name__ == "__main__":
    filename = "../resources/part12.txt"
    grid = read_input(filename)
    score = part_one(grid)
    score2 = part_two(grid)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")
