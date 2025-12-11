from math import prod
from itertools import combinations


def parse(name="input.txt"):
    points = []
    with open(name) as f:
        for line in f:
            points.append(tuple(map(int, line.strip().split(","))))
    return points


def area(a, b):
    return prod([abs(a[i] - b[i]) + 1 for i in range(len(a))])


def part1(points):
    pairs = combinations(points, 2)
    areas = [area(*pair) for pair in pairs]
    return max(areas)


points = parse("ex_input.txt")
assert 50 == part1(points)

points = parse()
print(part1(points))

