
def parse(file="input.txt"):
    with open(file, "r") as f:
        grid = [[int(c) for c in l.strip()] for l in f]

    trailheads = [
        complex(int(row), int(col))
        for row in range(len(grid))
        for col in range(len(grid[row]))
        if grid[row][col] == 0
    ]

    return grid, trailheads


def neighbors(grid, point):
    n_points = [point + 1, point - 1, point + 1j, point - 1j]
    return [
        n for n in [point + 1, point - 1, point + 1j, point - 1j]
        if 0 <= n.real < len(grid) 
         and 0 <= n.imag < len(grid[int(n.real)])
         and grid[int(n.real)][int(n.imag)] == grid[int(point.real)][int(point.imag)] + 1
    ]


def part1_score(head, grid):
    queue = [head]
    ends = []

    while queue:
        curr = queue.pop(0)
        for n in neighbors(grid, curr):
            if grid[int(n.real)][int(n.imag)] == 9:
                ends.append(n)
            else:
                queue.append(n)

    return len(set(ends))


def part2_score(head, grid):
    queue = [head]
    score = 0

    while queue:
        curr = queue.pop(0)
        for n in neighbors(grid, curr):
            if grid[int(n.real)][int(n.imag)] == 9:
                score += 1
            else:
                queue.append(n)

    return score

def part1(grid, trailheads):
    return sum([
        part1_score(head, grid)
        for head in trailheads
    ])

def part2(grid, trailheads):
    return sum([
        part2_score(head, grid)
        for head in trailheads
    ])


grid, trailheads = parse()
print(part1(grid, trailheads))
print(part2(grid, trailheads))

