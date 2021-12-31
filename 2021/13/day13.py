

class Grid:

    def __init__(self):
        self.points = []
        self.instructions = []
        with open("day13extended.txt") as f:
            for line in f:
                if "," in line:
                    self.points.append(tuple([int(c) for c in line.strip().split(",")]))
                elif "fold" in line:
                    axis = line.split(" ")[2].split("=")
                    self.instructions.append((axis[0], int(axis[1])))

    def fold(self, steps=None):
        if steps is None:
            steps = len(self.instructions)
        for instr in self.instructions[0:steps]:
            axis = instr[1]
            if instr[0] == "x":
                moving_points = [p for p in self.points if p[0] > axis]
                moved_points = [((2 * axis) - p[0], p[1]) for p in
                                moving_points]
            else:
                moving_points = [p for p in self.points if p[1] > axis]
                moved_points = [(p[0], (2 * axis) - p[1]) for p in
                                moving_points]
            self.points = list(set(self.points) - set(moving_points))
            self.points.extend(moved_points)
            self.points = list(set(self.points))

    @property
    def point_count(self):
        return len(self.points)

    def __str__(self):
        width = max([p[0] for p in self.points]) + 1
        height = max([p[1] for p in self.points]) + 1

        grid = [["."] * width for _ in range(height)]

        for p in self.points:
            grid[p[1]][p[0]] = "#"

        return "\n".join(["".join(r) for r in grid])


def day13A():
    grid = Grid()
    grid.fold(1)
    return grid.point_count


def day13B():
    grid = Grid()
    grid.fold()
    return str(grid)


if __name__ == "__main__":
    print(day13A())
    print(day13B())
