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


def dump(tiles, width, height):
    for j in range(height+1):
        for i in range(width+1):
            if (i, j) in tiles:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part1(points):
    pairs = combinations(points, 2)
    areas = [area(*pair) for pair in pairs]
    return max(areas)


def part2(red_tiles):
    min_width = min([p[0] for p in red_tiles])
    min_height = min([p[1] for p in red_tiles])
    width = max([p[0] for p in red_tiles])
    height = max([p[1] for p in red_tiles])

    all_tiles = set(red_tiles)
    # for each red pair, add the line between
    red_pairs = []
    for i in range(len(red_tiles)):
        red_pairs.append((red_tiles[i], red_tiles[(i+1) % len(red_tiles)]))
    for a, b in red_pairs:
        if a[0] == b[0]:
            all_tiles |= set([(a[0], i) for i in range(min(a[1], b[1]), max(a[1], b[1]))])
        elif a[1] == b[1]:
            all_tiles |= set([(i, a[1]) for i in range(min(a[0], b[0]), max(a[0], b[0]))])

    def rect_in(edges, a, b):
        width = min(a[0], b[0]), max(a[0], b[0])
        height = min(a[1], b[1]), max(a[1], b[1])

        # check if any edges are in the interior of the rect
        for e in edges:
            if (
                width[0] < e[0] < width[1] and
                height[0] < e[1] < height[1]
            ):
                return False

        return True

    pairs = combinations(red_tiles, 2)
    valid_pairs = [pair for pair in sorted(pairs) if rect_in(all_tiles, *pair)]
    areas = [area(*p) for p in valid_pairs]
    return max(areas)

points = parse("ex_input.txt")
assert 50 == part1(points)
assert 24 == part2(points)

points = parse()
print(part1(points))
print(part2(points))

