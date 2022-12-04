from math import cos, sin, pi
import numpy as np
import sys
from copy import deepcopy




def read_input(filename: str):
    materials = {}
    with open(filename, 'r') as file:
        missing = int(next(file).strip().split(" ")[0])
        for line in file:
            material = line.rstrip('\n').split(": ")
            components = material[1].split(", ")
            component_list = []
            for component in components:
                currComponent = component.split(" ")
                currAmount = int(currComponent[0])
                currMaterial = currComponent[1]
                component_list.append((currAmount, currMaterial))
            materials[material[0]] = component_list
    return missing, materials


updated_map = {}
is_component = set()

def n_materials(material, all_materials):
    components = all_materials[material]
    total = 0
    for component in components:
        if component[1] in updated_map:
            total += component[0] * updated_map[component[1]]
        elif component[1] in all_materials:
            is_component.add(component[1])
            total += component[0] * n_materials(component[1], all_materials)
        else:
            total += component[0]
    updated_map[material] = total
    return total


def part_one(content):
    materials = [n_materials(material, content) for material in content.keys()]
    return max(materials)

def brute_force(to_sum, start, values, solution):
    if sum(solution) == to_sum and len(solution) == 20:
        return True, solution
    elif sum(solution) > to_sum or len(solution) > 20:
        return False, solution
    total_sum = start
    found = False
    end_solution = None
    for value in values:
        total_sum += value
        solution.append(value)
        if brute_force(to_sum, total_sum, values, solution)[0]:
            end_solution = solution
            found = True
            break
        total_sum = start
        del solution[-1]
    return found, end_solution



#Convert problem to subset problem
def part_two(missing, content):
    updated_copy = deepcopy(updated_map)
    print(updated_copy)
    for k in list(updated_copy.keys()):
        if k in is_component:
            del updated_copy[k]
    #Store the reverse
    r_updated_copy = {v : k for k,v in updated_copy.items()}

    numbers = list(updated_copy.values())
    solution = brute_force(missing, sum(numbers), sorted(numbers,reverse=True), numbers)[1]
    cadeaus = sorted([r_updated_copy[x] for x in solution])

    word = ""
    for cadeau in cadeaus:
        word += cadeau[0]
    return word



if __name__ == "__main__":
    filename = "../resources/infi_2.txt"
    missing, content = read_input(filename)
    score = part_one(content)
    letters = part_two(missing, content)
    print(f"Most elements: {score}")
    print(f"Letters: {letters}")


