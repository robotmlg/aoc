from collections import defaultdict
from itertools import permutations

def parse(file="input.txt"):
    with open(file, "r") as f:
        grid = [list(l.strip()) for l in f]

    antennae = defaultdict(set)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            c = grid[row][col]
            if c.isalnum():
                antennae[c].add(complex(row, col))

    return antennae, len(grid), len(grid[0])


def part1(nodes_map, height, width):
    antinodes = defaultdict(set)
    for k, nodes in nodes_map.items():
        for node_pair in permutations(nodes, 2):  # get each node ordering separately
            delta = node_pair[1] - node_pair[0]
            a = node_pair[1] + delta
            if 0 <= a.real < height and 0 <= a.imag < width:
                antinodes[k].add(a)
    return set.union(*antinodes.values())


def part2(nodes_map, height, width):
    antinodes = defaultdict(set)
    for k, nodes in nodes_map.items():
        for node_pair in permutations(nodes, 2):  # get each node ordering separately
            delta = node_pair[1] - node_pair[0]

            for i in range(-50, 50):
                a = node_pair[0] + delta * i
                if 0 <= a.real < height and 0 <= a.imag < width:
                    antinodes[k].add(a)
    return set.union(*antinodes.values())


antennae, height, width = parse()
print(len(part1(antennae, height, width)))
print(len(part2(antennae, height, width)))

