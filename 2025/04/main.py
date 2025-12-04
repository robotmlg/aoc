
def parse(name="input.txt"):
    rows = []
    with open(name) as f:
        for line in f:
            rows.append([True if c == "@" else False for c in list(line.strip())])

    return rows


def count_neighbors(row, col, rolls):
    rows = len(rolls)
    cols = len(rolls[0])

    on_north_edge = row == 0
    on_east_edge = col == cols - 1
    on_south_edge = row == rows - 1
    on_west_edge = col == 0

    return sum([
        (not on_north_edge and rolls[row - 1][col]), # north
        (not on_north_edge and not on_east_edge and rolls[row - 1][col + 1]), # north east
        (not on_east_edge and rolls[row][col + 1]), # east
        (not on_south_edge and not on_east_edge and rolls[row + 1][col + 1]), # south east
        (not on_south_edge and rolls[row + 1][col]), # south
        (not on_south_edge and not on_west_edge and rolls[row + 1][col - 1]), # south west
        (not on_west_edge and rolls[row][col - 1]), # west
        (not on_north_edge and not on_west_edge and rolls[row - 1][col - 1]), # northwest
    ])


def part1(rolls):
    return sum([count_neighbors(row, col, rolls) < 4 for row in range(len(rolls)) for col in range(len(rolls[row])) if rolls[row][col]])


def part2(rolls):
    total = 0
    new_rolls = rolls

    while True:
        accessible_grid = [
            [count_neighbors(row, col, new_rolls) < 4 and new_rolls[row][col] 
            for col in range(len(new_rolls[row]))]
            for row in range(len(new_rolls))
        ]
        accessible = sum([x for row in accessible_grid for x in row])
        if accessible == 0:
            break

        new_rolls = [
            [
                new_rolls[row][col] and not accessible_grid[row][col]
                for col in range(len(new_rolls[row]))
            ]
            for row in range(len(new_rolls))
        ]

        total += accessible

    return total


rolls = parse()
print(part1(rolls))
print(part2(rolls))
