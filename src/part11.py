import collections
import copy
import re
from collections import deque
import numpy as np
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list
    operation: str
    test: int
    t_monkey: int
    f_monkey: int


    def eval_operation(self, old):
        return eval(self.operation)





def read_input(filename: str):
    monkeys = []
    with open(filename, 'r') as file:
        r_monkeys = file.read().strip().split('\n\n')
        for monkey in r_monkeys:
            details = monkey.split('\n')
            s_items = list(map(int, re.findall(r'\d+', details[1])))
            operation = details[2].split(' = ')[1]
            test = int(re.findall(r'\d+', details[3])[0])
            t_monkey = int(re.findall(r'\d', details[4])[0])
            f_monkey = int(re.findall(r'\d', details[5])[0])
            curr_monkey = Monkey(s_items, operation, test, t_monkey, f_monkey)
            monkeys.append(curr_monkey)
    return monkeys


def part_one(monkeys: list[Monkey]):
    rounds = 20
    inspections = [0] * len(monkeys)
    for curr_round in range(rounds):
        for i, monkey in enumerate(monkeys):
            inspections[i] += len(monkey.items)
            while len(monkey.items) > 0:
                worry = monkey.eval_operation(monkey.items[0])
                worry = worry // 3
                if worry % monkey.test == 0:
                    monkeys[monkey.t_monkey].items.append(worry)
                else:
                    monkeys[monkey.f_monkey].items.append(worry)
                #Remove current element
                monkey.items.pop(0)
    sorted_inspections = sorted(inspections, reverse=True)
    return sorted_inspections[0] * sorted_inspections[1]



def part_two(monkeys: list[Monkey]):
    div = [m.test for m in monkeys]

    #Get modulo number
    m = 1
    for i in div:
        m *= i
    rounds = 10000
    inspections = [0] * len(monkeys)
    for curr_round in range(rounds):
        for i, monkey in enumerate(monkeys):
            inspections[i] += len(monkey.items)
            while len(monkey.items) > 0:
                worry = monkey.eval_operation(monkey.items[0])
                worry %= m
                if worry % monkey.test == 0:
                    monkeys[monkey.t_monkey].items.append(worry)
                else:
                    monkeys[monkey.f_monkey].items.append(worry)
                #Remove current element
                monkey.items.pop(0)
    sorted_inspections = sorted(inspections, reverse=True)
    return sorted_inspections[0] * sorted_inspections[1]


if __name__ == "__main__":
    filename = "../resources/part11.txt"
    monkeys = read_input(filename)
    score = part_one(copy.deepcopy(monkeys))
    score2 = part_two(monkeys)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")

