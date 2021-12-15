import sys
from queue import PriorityQueue


def parse_input():
    with open("day15.txt") as f:
        grid = []
        for line in f:
            row = [int(c) for c in line.strip()]
            grid.append(row)

    return grid


def expand_grid(grid, size):
    def inc_and_wrap(start, inc):
        val = start + inc
        if val > 9:
            val -= 9
        return val

    # expand rows
    wide_grid = []
    for row in grid:
        new_row = list(row)
        for i in range(1, size):
            new_segment = list(map(lambda x: inc_and_wrap(x, i), row))
            new_row.extend(new_segment)
        wide_grid.append(new_row)

    # expand columns
    new_grid = list(wide_grid)
    for i in range(1, size):
        for row in wide_grid:
            new_row = list(map(lambda x: inc_and_wrap(x, i), row))
            new_grid.append(new_row)

    return new_grid


def dijkstra(grid):

    q = PriorityQueue()
    dist = {}
    prev = {}

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            point = (i, j)
            dist[point] = sys.maxsize
            prev[point] = None

    dist[(0, 0)] = 0
    q.put((0, (0, 0)))

    while q:
        p_dist, point = q.get()
        if point == (len(grid) - 1, len(grid[0]) - 1):
            return p_dist
        possible_neighbors = [
            (point[0] - 1, point[1]),
            (point[0], point[1] - 1),
            (point[0] + 1, point[1]),
            (point[0], point[1] + 1),
        ]
        neighbors = [p for p in possible_neighbors if 0 <= p[0] < len(grid)
                     and 0 <= p[1] < len(grid[0])]

        for n in neighbors:
            n_dist = p_dist + grid[point[0]][point[1]]
            if n_dist < dist[n]:
                dist[n] = n_dist
                prev[n] = point
                q.put((n_dist, n))

    raise Exception


if __name__ == "__main__":
    data = parse_input()
    print(dijkstra(data))
    print(dijkstra(expand_grid(data, 5)))
