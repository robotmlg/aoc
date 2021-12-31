ON = "on"
OFF = "off"


class Step:

    def __init__(self, line):
        self.op, dims = line.strip().split(" ")
        self.dims = []
        for dim in dims.split(","):
            vals = list(map(int, dim[2:].split("..")))
            self.dims.append((min(vals), max(vals)))


def parse_input(filename):
    steps = []
    with open(filename) as f:
        for line in f:
            steps.append(Step(line))
    return steps


def day22(steps, size):
    cubes = [[[0 for _ in range(-size, size + 1)]
              for __ in range(-size, size + 1)]
             for ___ in range(-size, size + 1)]

    for step in steps:
        op = 1 if step.op == ON else 0
        for x in range(-size, size + 1):
            for y in range(-size, size + 1):
                for z in range(-size, size + 1):
                    if (step.dims[0][0] <= x <= step.dims[0][1] and
                            step.dims[1][0] <= y <= step.dims[1][1] and
                            step.dims[2][0] <= z <= step.dims[2][1]):
                        cubes[x][y][z] = op

    return sum([sum([sum([z for z in y]) for y in x]) for x in cubes])


if __name__ == "__main__":
    print(day22(parse_input("day22.txt"), 50))
