def parse(file="input.txt"):
    with open(file, "r") as f:
        grid = [list(l.strip()) for l in f]

    regions = []
    searched = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            point = complex(row, col)
             
            if point not in searched:
                region = fill_region(point, grid)
                searched.extend(region)
                regions.append(region)
    return regions, len(grid[0]), len(grid)


def fill_region(point, grid):
    value = grid[int(point.real)][int(point.imag)]

    region = [point]
    queue = [point]
    while queue:
        p = queue.pop(0)
        p_n = neighbors(p, len(grid[0]), len(grid))
        for n in p_n:
            if n in region:
                continue
            if value == grid[int(n.real)][int(n.imag)]:
                region.append(n)
                queue.append(n)
    return region


def neighbors(point, width, height):
    return [
        n for n in [point + 1, point - 1, point + 1j, point - 1j]
        if 0 <= n.real < height and 0 <= n.imag < width
    ]


def fences(region, width, height):
    fences = [
        (p, f)
        for p in region
        for f in set([p + 1, p - 1, p + 1j, p - 1j]) - set([n for n in neighbors(p, width, height) if n in region])
    ]
    return fences


def sides(region, width, height):
    fs = fences(region, width, height)
    groups = []

    while fs:
        t = fs.pop()
        p, f = t
        side = [f]

        # edge direction is perpendicular to point->fence,
        # i.e. point->fence rotated 90
        f_direction = (f - p) * 1j

        for d in [f_direction, -f_direction]:
            for i in range(1, max(width, height)):
                t2 = (p + i * d, f + i * d)
                if t2 in fs:
                    fs.remove(t2)
                    side.append(t2)
                else:
                    break
        groups.append(side)

    return groups


regions, width, height = parse("input.txt")
print(sum([
    len(r) * len(fences(r, width, height))
    for r in regions
]))
print(sum([
    len(r) * len(sides(r, width, height))
    for r in regions
]))

