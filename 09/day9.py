from functools import reduce
from operator import mul


def day9():
    with open("day9.txt") as f:
        grid = [[int(c) for c in list(s.strip())] for s in f.readlines()]
        basin_map = [[' ' for _ in range(len(grid[i]))]
                     for i in range(len(grid))]

        risk_sum = 0
        basin_sizes = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                depth = grid[i][j]
                neighbors = []

                if i > 0:
                    neighbors.append(grid[i - 1][j])
                if i < len(grid) - 1:
                    neighbors.append(grid[i + 1][j])
                if j > 0:
                    neighbors.append(grid[i][j - 1])
                if j < len(grid[i]) - 1:
                    neighbors.append(grid[i][j + 1])

                if all(map(lambda n: n > depth, neighbors)):
                    risk_sum += (depth + 1)
                    # now that we know it's a low point, flow the basin
                    basin_queue = [(i, j)]
                    checked_basin = []

                    while basin_queue:
                        point = basin_queue.pop(0)
                        x, y = point
                        basin_map[x][y] = 'X'
                        checked_basin.append(point)

                        if (x > 0 and grid[x - 1][y] != 9 and
                                (x - 1, y) not in checked_basin and
                                (x - 1, y) not in basin_queue):
                            basin_queue.append((x - 1, y))
                        if (x < len(grid) - 1 and grid[x + 1][y] != 9 and
                                (x + 1, y) not in checked_basin and
                                (x + 1, y) not in basin_queue):
                            basin_queue.append((x + 1, y))
                        if (y > 0 and grid[x][y - 1] != 9 and
                                (x, y - 1) not in checked_basin and
                                (x, y - 1) not in basin_queue):
                            basin_queue.append((x, y - 1))
                        if (y < len(grid[x]) - 1 and grid[x][y + 1] != 9 and
                                (x, y + 1) not in checked_basin and
                                (x, y + 1) not in basin_queue):
                            basin_queue.append((x, y + 1))

                    basin_sizes.append(len(checked_basin))

        # print out the basins for fun
        print("\n".join([" ".join(i) for i in basin_map]))
        return risk_sum, reduce(mul, sorted(basin_sizes, reverse=True)[0:3], 1)


if __name__ == "__main__":
    print(day9())
