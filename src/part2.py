def read_input(filename: str):
    games = []
    with open(filename, 'r') as file:
        for line in file:
            game = line.strip().split(" ")
            games.append((game[0], game[1]))
    return games


def part_one(games: list[tuple[str, str]]):
    total_score = 0
    win_scores = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0, ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
                  ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}
    select_scores = {'X': 1, 'Y': 2, 'Z': 3}
    for game in games:
        total_score += win_scores[game] + select_scores[game[1]]
    return total_score

def part_two(games: list[tuple[str, str]]):
    total_score = 0
    to_lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    to_draw ={'A': 'X', 'B': 'Y', 'C': 'Z'}
    to_win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    win_scores = {'X': 0, 'Y': 3, 'Z': 6}
    select_scores = {'X': 1, 'Y': 2, 'Z': 3}
    for opponent, you in games:
        if you == 'X':
            total_score += win_scores[you] + select_scores[to_lose[opponent]]
        elif you == 'Y':
            total_score += win_scores[you] + select_scores[to_draw[opponent]]
        elif you == 'Z':
            total_score += win_scores[you] + select_scores[to_win[opponent]]
    return total_score


if __name__ == "__main__":
    filename = "../resources/part2.txt"
    games = read_input(filename)
    score = part_one(games)
    score2 = part_two(games)
    print(f"Part one: {score}")
    print(f"Part two: {score2}")

