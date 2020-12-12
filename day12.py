import timeit
from itertools import product
from collections import defaultdict


def load_data():
    with open(input_file, 'r') as f:
        data = f.read().strip().split()
    return data


def parse_data():
    pass


action_mapping = {
    # action: (dx, dy)
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}
directions = 'NESW'


def part1():
    x, y = 0, 0
    facing_direction = 'E'
    for instruction in data:
        action, value = instruction[0], int(instruction[1:])
        if action in 'NESW':
            dx, dy = action_mapping[action]
            x, y = x + value * dx, y + value * dy
        elif action in 'LR':
            turns_of_90 = value // 90
            direction_index = directions.index(facing_direction)
            new_direction_index = (direction_index - turns_of_90) % 4 if action == 'L' else \
                                  (direction_index + turns_of_90) % 4
            facing_direction = directions[new_direction_index]
        elif action == 'F':
            dx, dy = action_mapping[facing_direction]
            x, y = x + value * dx, y + value * dy
        else:
            ValueError()

    return abs(x) + abs(y)


def part2():
    x, y = 0, 0
    waypoint_x, waypoint_y = 10, 1  # is direction of dx, dy
    for instruction in data:
        print(x, y, waypoint_x, waypoint_y)
        print(instruction)
        print()
        action, value = instruction[0], int(instruction[1:])
        if action in 'NESW':
            waypoint_dx, waypoint_dy = action_mapping[action]
            waypoint_x, waypoint_y = waypoint_x + value * waypoint_dx, waypoint_y + value * waypoint_dy
        elif action == 'L':
            if value == 180:
                waypoint_x, waypoint_y = -1 * waypoint_x, -1 * waypoint_y
            elif value in [90, 270]:
                # first determine the magnitudes
                magnitude_x, magnitude_y = abs(waypoint_y), abs(waypoint_x)

                # then determine the sign
                sign_x, sign_y = 1, 1
                if value == 90:
                    if waypoint_y >= 0:
                        sign_x = -1
                    if waypoint_x <= 0:
                        sign_y = -1
                else:
                    if waypoint_y <= 0:
                        sign_x = -1
                    if waypoint_x >= 0:
                        sign_y = -1

                waypoint_x, waypoint_y = sign_x * magnitude_x, sign_y * magnitude_y
            else:
                NotImplementedError()

        elif action == 'R':
            if value == 180:
                waypoint_x, waypoint_y = -1 * waypoint_x, -1 * waypoint_y
            elif value in [90, 270]:
                # first determine the magnitudes
                magnitude_x, magnitude_y = abs(waypoint_y), abs(waypoint_x)

                # then determine the sign
                sign_x, sign_y = 1, 1
                if value == 270:
                    if waypoint_y >= 0:
                        sign_x = -1
                    if waypoint_x <= 0:
                        sign_y = -1
                else:
                    if waypoint_y <= 0:
                        sign_x = -1
                    if waypoint_x >= 0:
                        sign_y = -1

                waypoint_x, waypoint_y = sign_x * magnitude_x, sign_y * magnitude_y

            else:
                NotImplementedError()
        elif action == 'F':
            x, y = x + value * waypoint_x, y + value * waypoint_y
        else:
            ValueError()

    print(x ,y)

    return abs(x) + abs(y)


def main():
    a1 = part1()
    print(a1)

    a2 = part2()
    print(a2)


if __name__ == '__main__':
    input_file = 'input12.txt'
    data = load_data()
    parsed = parse_data()
    main()

    # t = timeit.Timer('part1(p1=False)', globals=globals())
    # n = 100
    # print(sum(t.repeat(repeat=n, number=1)) / n)
