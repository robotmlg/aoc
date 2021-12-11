
class Dumbo:

    def __init__(self, energy: int):
        self.energy = energy
        self.neighbors = []
        self.flashed = False

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def increment(self):
        if not self.flashed:
            self.energy += 1

            if self.energy > 9:
                self.flashed = True
                for n in self.neighbors:
                    n.increment()

    def reset(self):
        self.flashed = False
        if self.energy > 9:
            self.energy = 0


class Grid:

    def __init__(self):
        grid = []
        with open("day11.txt") as f:
            for line in f:
                grid.append([Dumbo(int(n)) for n in line.strip()])

        self.height = len(grid)
        self.width = len(grid[0])

        # populate neighbors
        for i in range(self.height):
            for j in range(self.width):
                if i > 0 and j > 0:
                    """
                    X00
                    0.0
                    000
                    """
                    grid[i][j].add_neighbor(grid[i - 1][j - 1])
                if i > 0:
                    """
                    0X0
                    0.0
                    000
                    """
                    grid[i][j].add_neighbor(grid[i - 1][j])
                if j > 0:
                    """
                    000
                    X.0
                    000
                    """
                    grid[i][j].add_neighbor(grid[i][j - 1])
                if i < self.height - 1 and j < self.width - 1:
                    """
                    000
                    0.0
                    00X
                    """
                    grid[i][j].add_neighbor(grid[i + 1][j + 1])
                if i < self.height - 1:
                    """
                    000
                    0.0
                    0X0
                    """
                    grid[i][j].add_neighbor(grid[i + 1][j])
                if j < self.width - 1:
                    """
                    000
                    0.X
                    000
                    """
                    grid[i][j].add_neighbor(grid[i][j + 1])
                if i < self.height - 1 and j > 0:
                    """
                    000
                    0.0
                    X00
                    """
                    grid[i][j].add_neighbor(grid[i + 1][j - 1])
                if i > 0 and j < self.width - 1:
                    """
                    00X
                    0.0
                    000
                    """
                    grid[i][j].add_neighbor(grid[i - 1][j + 1])

        # now that we've determined the neighbors, unroll the grid to make it
        # easier to work with
        self.octopodes = [d for ds in grid for d in ds]

    def step(self, ticks: int = 0):
        total_flashes = 0
        first_sync = None
        for tick in range(1, ticks + 1):
            # can't use map() here because map() returns a generator
            # could do list(map()) but that's ugly IMO
            [o.increment() for o in self.octopodes]
            flashes = sum([1 if o.flashed else 0 for o in self.octopodes])
            total_flashes += flashes
            if flashes == self.width * self.height and first_sync is None:
                first_sync = tick
            [o.reset() for o in self.octopodes]
        return total_flashes, first_sync

    def print_grid(self):
        print("\n".join(["|".join([
            str(self.octopodes[i * self.width + j].energy)
            for j in range(self.width)])
            for i in range(self.height)]))


def day11A():
    return Grid().step(100)


def day11B():
    return Grid().step(1000)


if __name__ == "__main__":
    print(day11A())
    print(day11B())
