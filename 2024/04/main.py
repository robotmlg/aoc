
def parse():
    lines = []
    with open("input.txt", "r") as f:
        for l in f:
            lines.append(list(l))
    return lines


def find_words(grid, start_row, start_col, word):
    letters = list(word)
    if grid[start_row][start_col] != letters[0]:
        return False

    def check_direction(delta, name):
        try:
            for i in range(1, len(letters)):
                if not 0 <= start_row + delta[0]*i < len(grid):
                    return 0
                if not 0 <= start_col + delta[1]*i < len(grid[start_row]):
                    return 0
                if grid[start_row + delta[0]*i][start_col + delta[1]*i]  != letters[i]:
                    return 0
            # print(f"Found at row {start_row} col {start_col} going {name}")
            return 1
        except IndexError:
            return 0

    return sum([check_direction(f, n) for f, n in [
        ((0, 1), "east"),
        ((1, 0), "south"),
        ((0, -1), "west"),
        ((-1, 0), "north"),

        ((-1, 1), "northeast"),
        ((1, -1), "southeast"),
        ((1, 1), "southwest"),
        ((-1, -1), "northwest"),
    ]]
    )


def part1(grid):
    return sum([
        find_words(grid, row, col, "XMAS")
        for row in range(len(grid))
        for col in range(len(grid[row]))
    ])


def part2(grid):
    return sum([
        grid[row][col] == "A" and
        (
            [grid[row+1][col+1], grid[row+1][col-1], grid[row-1][col-1], grid[row-1][col+1]] == ["S", "S", "M", "M"] or
            [grid[row+1][col+1], grid[row+1][col-1], grid[row-1][col-1], grid[row-1][col+1]] == ["M", "S", "S", "M"] or
            [grid[row+1][col+1], grid[row+1][col-1], grid[row-1][col-1], grid[row-1][col+1]] == ["M", "M", "S", "S"] or
            [grid[row+1][col+1], grid[row+1][col-1], grid[row-1][col-1], grid[row-1][col+1]] == ["S", "M", "M", "S"]
        )
        for row in range(1, len(grid) - 1)
        for col in range(1, len(grid[row]) - 1)
    ])


grid = parse()
print(part1(grid))
print(part2(grid))
 
