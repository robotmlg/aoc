from math import copysign

class Step():
    
    def __init__(self, line: str):
        self.direction = line[0]
        self.distance = int(line[2:-1])


class Rope():

    def __init__(self, length : int = 0):
        self.knots = [(0,0)] * length
        self.visited = {(0,0)}

    def apply(self, step):
        for _ in range(0, step.distance):
            # move the head
            match step.direction:
                case "U":
                    self.knots[0] = (self.knots[0][0], self.knots[0][1] + 1)
                case "D":
                    self.knots[0] = (self.knots[0][0], self.knots[0][1] - 1)
                case "L":
                    self.knots[0] = (self.knots[0][0] - 1, self.knots[0][1])
                case "R":
                    self.knots[0] = (self.knots[0][0] + 1, self.knots[0][1])
                case _:
                    raise Exception
            # resolve the knots
            for i in range(1, len(self.knots)):
                x_dist = self.knots[i-1][0] - self.knots[i][0]
                y_dist = self.knots[i-1][1] - self.knots[i][1]

                # no movement if touching
                if abs(x_dist) <= 1 and abs(y_dist) <= 1:
                    continue

                """
                # this doesn't work for part 2, but it does on the pt 2 sample input, but I can't figure out why
                if abs(x_dist) == 2:
                    self.knots[i] = (self.knots[i][0] + copysign(1, x_dist), self.knots[i][1])
                    if abs(y_dist) == 1:
                        self.knots[i] = (self.knots[i][0], self.knots[i][1] + copysign(1, y_dist))
                elif abs(y_dist) == 2:
                    self.knots[i] = (self.knots[i][0], self.knots[i][1] + copysign(1, y_dist))
                    if abs(x_dist) == 1:
                        self.knots[i] = (self.knots[i][0] + copysign(1, x_dist), self.knots[i][1])
                """

                self.knots[i] = (
                    int(self.knots[i][0] if x_dist == 0 else self.knots[i][0] + copysign(1, x_dist)),
                    int(self.knots[i][1] if y_dist == 0 else self.knots[i][1] + copysign(1, y_dist))
                )
            self.visited.add(self.knots[-1])


def parse_input():
    steps = []
    with open("in.txt") as f:
        for line in f:
            steps.append(Step(line))
    return steps


def part1(steps):
    rope = Rope(2)

    for step in steps:
        rope.apply(step)

    return len(rope.visited)


def part2(steps):
    rope = Rope(10)

    for step in steps:
        rope.apply(step)

    return len(rope.visited)


def main():
    steps = parse_input()
    print(part1(steps))
    print(part2(steps))


main()
