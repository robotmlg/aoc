import math


class Line:

    def __init__(self, input: str):
        parsed = input.split(" ")
        self.p = self._parse_point(parsed[0])
        # skip the -> at index 1
        self.q = self._parse_point(parsed[2])

    def is_orthogonal(self) -> bool:
        return (self.p[0] == self.q[0] or
                self.p[1] == self.q[1])

    def get_points(self) -> list[tuple]:
        # horizontal
        if self.p[0] == self.q[0]:
            return [(self.p[0], y) for y in range(min(self.p[1], self.q[1]),
                                                  max(self.p[1], self.q[1]) + 1
                                                  )]
        # vertical
        elif self.p[1] == self.q[1]:
            return [(x, self.p[1]) for x in range(min(self.p[0], self.q[0]),
                                                  max(self.p[0], self.q[0]) + 1
                                                  )]
        # diagonal
        if self.p[0] < self.q[0]:
            slope = int((self.q[1] - self.p[1]) / (self.q[0] - self.p[0]))
            left, right = self.p, self.q
        else:
            slope = int((self.p[1] - self.q[1]) / (self.p[0] - self.q[0]))
            left, right = self.q, self.p
        return list(zip(range(left[0], right[0] + 1),
                        range(left[1], right[1] + (slope * 1), slope)))

    @staticmethod
    def _parse_point(input: str) -> tuple[int]:
        return tuple(map(lambda i: int(i), input.split(',')))


class Grid:

    def __init__(self):
        self.points = {}

    def mark_line(self, line: Line):
        for p in line.get_points():
            self.points[p] = self.points[p] + 1 if p in self.points else 1

    def get_overlap_count(self) -> int:
        return sum([1 for p in self.points.values() if p > 1])


def day5A():
    grid = Grid()
    with open("day5.txt") as f:
        for string in f:
            line = Line(string)
            if line.is_orthogonal():
                grid.mark_line(line)
    return grid.get_overlap_count()


def day5B():
    grid = Grid()
    with open("day5.txt") as f:
        for string in f:
            grid.mark_line(Line(string))
    return grid.get_overlap_count()


if __name__ == "__main__":
    print(day5A())
    print(day5B())
