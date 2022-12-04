from math import cos, sin, pi
import numpy as np
import sys
def read_input(filename: str):
    contents = []
    with open(filename, 'r') as file:
        for line in file:
            action = line.strip().split(" ")
            contents.append((action[0], int(action[1])))
    return contents

def angle_to_radian(angle):
    return angle * (pi / 180)

#Update the message array
def update_show(before, after, show):
    diffX = before[0] - after[0]
    diffY = before[1] - after[1]
    while before != after:
        x = before[1]
        y = before[0]
        show[x][y] = 'x'
        if diffX < 0:
            y += 1
        elif diffX > 0:
            y -= 1
        if diffY < 0:
            x += 1
        elif diffY > 0:
            x -= 1
        before = (y, x)
    #Set final point also
    show[before[1]][before[0]] = 'x'


def part_one(content):
    position = (0, 0)
    angle = 0
    angles_map = {0: (0, 1), 45: (0.5, 0.5), 90: (1, 0), 135:(0.5, -0.5), 180: (0, -1),
                  315: (-0.5, 0.5), 270: (-1 , 0), 225: (-0.5, -0.5)}

    #Initialize shape of message
    shape = (8, 100)
    show = np.empty(shape, dtype=object)
    for action, number in content:
        if action == "draai":
            if number < 0:
                number = 360 - abs(number)
            angle += number
            angle = angle % 360
        elif action == "loop":
            steps = angles_map[angle]
            #If diagonal step, perform twice at one
            if abs(steps[0]) == 0.5 or abs(steps[1]) == 0.5:
                x = position[0] + 2 * (steps[0] * number)
                y = position[1] + 2 * (steps[1] * number)
            else:
                x = position[0] + steps[0] * number
                y = position[1] + steps[1] * number
            update_show((int(x), int(y)), position, show)
            position = (x, y)
        elif action == "spring":
            steps = angles_map[angle]
            x = position[0] + steps[0] * number
            y = position[1] + steps[1] * number
            position = (x, y)

    #Rotate correctly to show 'KERSTPAKKET'
    show[show == None] = '-'
    show = np.rollaxis(show, axis =1)
    show = np.rot90(show)
    np.savetxt('../resources/message.txt', X=show, fmt='%s')

    return abs(position[0]) + abs(position[1])


if __name__ == "__main__":
    filename = "../resources/infi.txt"
    content = read_input(filename)
    score = part_one(content)
    print(f"Manhattan distance: {score}")


