
def read_input(filename: str):
    first = []
    second = []
    with open(filename, 'r') as file:
        for line in file:
            assignments = line.strip().split(",")
            first_a = assignments[0].split("-")
            first.append((int(first_a[0]), int(first_a[1])))
            second_a = assignments[1].split("-")
            second.append((int(second_a[0]), int(second_a[1])))
    return (first, second)
def part_one(content):
    overlaps = 0
    for first, second in zip(*content):
        rangeFirst = set(list(range(first[0], first[1] + 1)))
        rangeSecond = set(list(range(second[0], second[1] + 1)))
        overlap = rangeFirst & rangeSecond
        if len(overlap) == len(rangeFirst) or len(overlap) == len(rangeSecond):
            overlaps += 1
    return overlaps

def part_two(content):
    overlaps = 0
    for first, second in zip(*content):
        rangeFirst = set(list(range(first[0], first[1] + 1)))
        rangeSecond = set(list(range(second[0], second[1] + 1)))
        overlap = rangeFirst & rangeSecond
        if len(overlap) > 0:
            overlaps += 1
    return overlaps

if __name__ == "__main__":
    filename = "../resources/part4.txt"
    content = read_input(filename)
    score = part_one(content)
    score2 = part_two(content)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")

