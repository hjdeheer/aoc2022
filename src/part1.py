def read_input(filename: str):
    with open(filename, 'r') as file:
        content = file.read()
    elves = [[int(x) for x in elf.split('\n')] for elf in content.split('\n\n')]
    #elves = [list(map(int, elf.split('\n'))) for elf in content.split('\n\n')]
    return elves


def part_one(elves: list[list[int]]):
    elf_calories = [sum(elf) for elf in elves]
    return max(elf_calories)

def part_two(elves: list[list[int]]):
    elf_calories = [sum(elf) for elf in elves]
    elf_calories.sort(reverse=True)
    return sum(elf_calories[0:3])


if __name__ == "__main__":
    filename = "../resources/part1.txt"
    elves = read_input(filename)
    calories = part_one(elves)
    top3_calories = part_two(elves)
    print(f"Part one: {calories = }")
    print(f"Part two: {top3_calories = }")


