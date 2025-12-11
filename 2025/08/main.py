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


def build_circuit(points, target=None):
    pairs = combinations(points, 2)
    distances = {pair: dist(*pair) for pair in pairs}
    closest = sorted(distances.keys(), key=lambda p: distances[p])

    circuits = {}
    point_to_circuit = {}
    new_circuit_index = 0
    connections_made = 0
    unconnected_points = set(points)

    def in_circuit(point):
        return point_to_circuit.get(point) is not None

    if target is None:
        target = len(closest)

    for i in range(target):
        if not unconnected_points and len(circuits.keys()) == 1:
            break
        a, b = closest.pop(0)

        cir_a, cir_b  = point_to_circuit.get(a), point_to_circuit.get(b)

        if in_circuit(a) and in_circuit(b) and cir_a == cir_b:
            # both points are already in the same circuit, skip
            continue
        elif in_circuit(a) and in_circuit(b) and cir_a != cir_b:
            # if each point is in a different circuit, merge them
            for p in circuits[cir_b]:
                point_to_circuit[p] = cir_a
            circuits[cir_a] |= circuits[cir_b]
            del circuits[cir_b]
        # if one point is in a circuit, add the other, and count
        elif in_circuit(a) and not in_circuit(b):
            point_to_circuit[b] = cir_a
            circuits[cir_a].add(b)
        elif in_circuit(b) and not in_circuit(a):
            point_to_circuit[a] = cir_b
            circuits[cir_b].add(a)
        else:
            point_to_circuit[a] = new_circuit_index
            point_to_circuit[b] = new_circuit_index
            circuits[new_circuit_index] = set((a, b))
            new_circuit_index += 1

        if a in unconnected_points:
            unconnected_points.remove(a)
        if b in unconnected_points:
            unconnected_points.remove(b)

    return circuits, (a, b)


def part1(points, target=1000):
    circuits, last_pair = build_circuit(points, target)

    circuit_lengths = sorted([len(c) for c in circuits.values()])

    return prod(circuit_lengths[-3:])


def part2(points):
    circuits, last_pair = build_circuit(points)

    return last_pair[0][0] * last_pair[1][0]


points = parse("ex_input.txt")
assert 40 == part1(points, 10)
assert 25272 == part2(points)

points = parse()
print(part1(points))
print(part2(points))
