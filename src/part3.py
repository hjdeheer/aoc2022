
def read_input(filename: str):
    rucksacks = []
    with open(filename, 'r') as file:
        for line in file:
            rucksacks.append(line.strip())
    return rucksacks

def part_one(rucksacks: list[str]):
    total_sum = 0
    shared = []
    for rucksack in rucksacks:
        len_items = int(len(rucksack) / 2)
        first = rucksack[:len_items]
        second = rucksack[len_items:]
        first_component = {component for component in first}
        second_component = {component for component in second}
        both_component = first_component.intersection(second_component)
        shared.append(both_component.pop())
    for priority in shared:
        total_sum += ord(priority) - 38 if priority.isupper() else ord(priority) - 96
    return total_sum

def part_two(rucksacks: list[str]):
    total_sum = 0
    shared = []
    for i in range(2, len(rucksacks), 3):
        first_component = {component for component in rucksacks[i-2]}
        second_component = {component for component in rucksacks[i-1]}
        third_component = {component for component in rucksacks[i]}
        both_component = first_component.intersection(second_component, third_component)
        shared.append(both_component.pop())
    for priority in shared:
        total_sum += ord(priority) - 38 if priority.isupper() else ord(priority) - 96
    return total_sum


if __name__ == "__main__":
    filename = "../resources/part3.txt"
    rucksacks = read_input(filename)
    score = part_one(rucksacks)
    score2 = part_two(rucksacks)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")

