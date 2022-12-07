from __future__ import annotations
import collections
import copy
from collections import deque
from dataclasses import dataclass

@dataclass
class File:
    size: int
    name: str



@dataclass
class Dir:
    name: str
    size: int
    parent: Dir
    childs: list[Dir]
    files: list[File]







def read_input(filename: str):
    root = Dir(name='/', size=-1, parent=None, childs=[], files=[])
    curr = root
    #We are building a binary tree
    with open(filename, 'r') as file:
        commands = file.read().strip().split("$ ")
        for execution in commands[1:]:
            execution = execution.strip()
            lines = execution.split("\n")
            command = lines[0]
            if command[0:2] == 'cd':
                dir_op = command.split(" ")
                if dir_op[1] == '..':
                    curr = curr.parent
                elif dir_op[1] == '/':
                    curr = root
                else:
                    dir_name = dir_op[1]
                    for d in curr.childs:
                        if d.name == dir_name:
                            curr = d
            elif command[0:2] == 'ls':
                for param in lines[1:]:
                    file_or_dir = param.split(" ")
                    if file_or_dir[0] == 'dir':
                        curr.childs.append(Dir(name=file_or_dir[1], size=-1, parent=curr, childs=[], files=[]))
                    #Must be file
                    else:
                        curr.files.append(File(name=file_or_dir[1], size=int(file_or_dir[0])))
    print(root)
    return root




def build_sum(root: Dir):
    #Set sum of this dir
    if len(root.childs) == 0:
        size = 0
        for f in root.files:
            size += f.size
        root.size = size
        return size
    total_sum = 0
    for d in root.childs:
        total_sum += build_sum(d)
    for f in root.files:
        total_sum += f.size
    root.size = total_sum
    return total_sum

def traverse_one(root):
    if root.size > 100000 and len(root.childs) == 0:
        return 0
    total_sum = 0
    if root.size < 100000:
        total_sum += root.size
    for d in root.childs:
        total_sum += traverse_one(d)
    return total_sum


def traverse_two(root, deleted, best):
    if len(root.childs) == 0 and best > root.size > deleted:
        return root.size
    curr_best = best
    if best > root.size > deleted:
        curr_best = root.size
    for d in root.childs:
        curr_best = min(curr_best, traverse_two(d, deleted, curr_best))
    return curr_best


def part_one(root):
    build_sum(root)
    return traverse_one(root)


def part_two(root):
    build_sum(root)
    unused = 70000000 - root.size
    deleted = 30000000 - unused
    return traverse_two(root, deleted, float("inf"))


if __name__ == "__main__":
    filename = "../resources/part7.txt"
    root = read_input(filename)
    score = part_one(root)
    score2 = part_two(root)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")

