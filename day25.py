import timeit
from itertools import product
from collections import defaultdict


def load_data():
    with open(input_file, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def parse_data():
    pass


def part1():
    pass


def part2():
    pass


def main():
    a1 = part1()
    print(a1)

    a2 = part2()
    print(a2)


if __name__ == '__main__':
    input_file = 'input25.txt'
    data = load_data()
    parsed = parse_data()
    main()

    # t = timeit.Timer('part2()', globals=globals())
    # n = 30
    # print(sum(t.repeat(repeat=n, number=1)) / n)
