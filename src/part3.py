
def read_input(filename: str):
    with open(filename, 'r') as file:
        for line in file:
            return

def part_one(games):
    return

def part_two(games):
    return


if __name__ == "__main__":
    filename = "../resources/part3.txt"
    games = read_input(filename)
    score = part_one(games)
    score2 = part_two(games)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")

