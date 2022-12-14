

def parse_input():
    points = set()

    with open("in.txt") as f:
        for line in f:
            vertices = [tuple([int(c) for c in s.split(",")]) for s in line.strip().split(" -> ")]
            for i in range(1, len(vertices)):
                if vertices[i][0] == vertices[i-1][0]:
                    high = max(vertices[i][1], vertices[i-1][1])
                    low = min(vertices[i][1], vertices[i-1][1])

                    points.update([(vertices[i][0], j) for j in range(low, high+1)])
                elif vertices[i][1] == vertices[i-1][1]:
                    high = max(vertices[i][0], vertices[i-1][0])
                    low = min(vertices[i][0], vertices[i-1][0])

                    points.update([(j, vertices[i][1]) for j in range(low, high+1)])
                else:
                    raise Exception

    return points


def part1(rocks):
    rocks_and_sand = set(rocks)
    lowest_rock = max([r[1] for r in rocks_and_sand])
    sand = (500, 0)
    resting_sand = 0
    while True:
        if sand[1] > lowest_rock:
            return resting_sand
        if (sand[0], sand[1] + 1) not in rocks_and_sand:
            sand = (sand[0], sand[1] + 1)
        elif (sand[0] - 1, sand[1] + 1) not in rocks_and_sand:
            sand = (sand[0] - 1, sand[1] + 1)
        elif (sand[0] + 1, sand[1] + 1) not in rocks_and_sand:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            rocks_and_sand.add(sand)
            resting_sand += 1
            sand = (500, 0)


def part2(rocks):
    rocks_and_sand = set(rocks)
    floor = max([r[1] for r in rocks_and_sand]) + 2
    sand = (500, 0)
    resting_sand = 0
    while True:
        if sand[1] + 1 == floor:
            rocks_and_sand.add(sand)
            resting_sand += 1
            sand = (500, 0)
        if (sand[0], sand[1] + 1) not in rocks_and_sand:
            sand = (sand[0], sand[1] + 1)
        elif (sand[0] - 1, sand[1] + 1) not in rocks_and_sand:
            sand = (sand[0] - 1, sand[1] + 1)
        elif (sand[0] + 1, sand[1] + 1) not in rocks_and_sand:
            sand = (sand[0] + 1, sand[1] + 1)
        elif sand == (500, 0):
            rocks_and_sand.add(sand)
            resting_sand += 1
            return resting_sand
        else:
            rocks_and_sand.add(sand)
            resting_sand += 1
            sand = (500, 0)


def main():
    rocks = parse_input()
    print(part1(rocks))
    print(part2(rocks))
                

main()
