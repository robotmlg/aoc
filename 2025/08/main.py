from math import sqrt, prod
from itertools import combinations


def parse(name="input.txt"):
    points = []
    with open(name) as f:
        for line in f:
            points.append(tuple(map(int, line.strip().split(","))))
    return points


def dist(a, b):
    return sqrt(sum([(a[i] - b[i]) ** 2 for i in range(len(a))]))


def part1(points, target=1000):
    pairs = combinations(points, 2)
    distances = {pair: dist(*pair) for pair in pairs}
    closest = sorted(distances.keys(), key=lambda p: distances[p])

    circuits = []
    connections_made = 0
    while True:
        if connections_made == target:
            break
        pair = closest.pop(0)
        
        # find if any circuit contains one of the points
        for circuit in circuits:
            if pair[0] in circuit and pair[1] in circuit:
                # if both points are in a circuit, skip
                break
            if pair[0] in circuit or pair[1] in circuit:
                # if one point is in a circuit, add the other, and count
                circuit.add(pair[0])
                circuit.add(pair[1])
                connections_made += 1
                break
        else:
            # if you didn't add to an existing circuit, create a new circuit, and count
            circuits.append(set(pair))
            connections_made += 1

    circuit_lengths = sorted([len(c) for c in circuits])

    return prod(circuit_lengths[-3:])


points = parse("ex_input.txt")
assert 40 == part1(points, 10)

real_points = parse()
print(part1(real_points))
