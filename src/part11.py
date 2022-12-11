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
        r_monkeys = file.read().split('\n\n')
        for monkey in r_monkeys:
            details = monkey.strip().split('\n  ')
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




#11/13/17/19/23
# def fast_div(worry, by):
#     s_worry = str(worry)
#     numbers = [int(x) for x in s_worry]
#     if by == 2:
#         return int(numbers[-1]) % 2 == 0
#     elif by == 3:
#         return sum(numbers) % 3 == 0
#     elif by == 4:
#         return int(s_worry[-2:]) % 4 == 0
#     elif by == 5:
#         return int(numbers[-1]) == 5 or int(numbers[-1]) == 0
#     elif by == 6:
#         return fast_div(worry, 3) and fast_div(worry, 2)
#     elif by == 7:
#         curr_number = s_worry
#         while len(curr_number) > 1:
#             curr_number = str(int(s_worry[0:-1]) - 2 * int(curr_number[-1]))
#         return curr_number == '7' or curr_number == '0'
#     elif by == 9:
#         return sum(numbers) % 9 == 0
#     elif by == 11:
#         total = 0
#         for i, el in enumerate(numbers):
#             if i % 2 == 0:
#                 total += el
#             else:
#                 total -= el
#         return total % 11 == 0
#     elif by == 13:
#         curr_number = s_worry
#         while len(curr_number) > 2:
#             curr_number = str(int(curr_number[0:-1]) + 4 * int(curr_number[-1]))
#         return int(curr_number) % 13 == 0
#     elif by == 17:
#         curr_number = s_worry
#         while len(curr_number) > 2:
#             curr_number = str(int(curr_number[0:-1]) - 5 * int(curr_number[-1]))
#         return int(curr_number) % 17 == 0
#     elif by == 19:
#         curr_number = s_worry
#         while len(curr_number) > 2:
#             curr_number = str(int(curr_number[0:-1]) + 2 * int(curr_number[-1]))
#         return int(curr_number) % 19 == 0
#     elif by == 23:
#         curr_number = s_worry
#         while len(curr_number) > 2:
#             curr_number = str(int(curr_number[0:-1]) + 7 * int(curr_number[-1]))
#         return int(curr_number) % 23 == 0
#     else:
#         print(f"{by} not implemented")

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

