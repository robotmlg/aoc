from math import copysign
from unittest import TestCase


class Probe:

    def __init__(self,
                 v_0: tuple[int, int],
                 target: tuple[tuple[int, int], tuple[int, int]]):
        self.location = (0, 0)
        self.target = target
        self.velocity = v_0
        self.locations = [self.location]
        self.time = 0

    def step(self):
        self.location = (self.location[0] + self.velocity[0],
                         self.location[1] + self.velocity[1])
        self.velocity = (0 if self.velocity[0] == 0 else
                         copysign(abs(self.velocity[0] - 1), self.velocity[0]),
                         self.velocity[1] - 1)
        self.locations.append(self.location)
        self.time += 1

    @property
    def hit_x(self):
        return self.target[0][0] <= self.location[0] <= self.target[1][0]

    @property
    def hit_y(self):
        return self.target[0][1] <= self.location[1] <= self.target[1][1]

    @property
    def above(self):
        return any([l[1] > self.target[1][1]for l in self.locations])

    @property
    def below(self):
        return any([l[1] < self.target[0][1]for l in self.locations])

    @property
    def left(self):
        return any([l[0] < self.target[0][0]for l in self.locations])

    @property
    def right(self):
        return any([l[0] > self.target[1][0]for l in self.locations])


class ProbeChecker:

    def __init__(self, filename):
        self.target = self._get_target(filename)

    def max_height(self) -> int:
        """
        Lemmas:
        * You always hit the same heights on the way up as on the way down.
        * The fastest vertical speed will give the highest height
        * The maximum downward speed is that which will hit the bottom of the
          target in one step, self.target[0][1]
        * The upward speed that gives us that downward speed when passing
          through y=0 on the way down is -self.target[0][1] - 1
        * The maximum height is the sum from 0 to the initial velocity

        :return: the maximum height
        """
        return (abs(self.target[0][1]) - 1) * abs(self.target[0][1]) // 2

    def find_v0s(self) -> set[tuple[int, int]]:
        vys = []
        # find all the v0y values that will eventually hit
        for vy in range(self.target[0][1], -self.target[0][1] + 1):
            probe = Probe((0, vy), self.target)

            while True:
                probe.step()
                if probe.hit_y:
                    vys.append((vy, probe.time))
                # end when you've crossed over the target
                elif probe.above and probe.below:
                    break

        # only need to check v0xs that will hit within the vy time to hit
        max_time = max([vy[1] for vy in vys])
        vxs = []
        # find all the v0x values that will eventually hit
        for vx in range(1, self.target[1][0] + 1):
            probe = Probe((vx, 0), self.target)

            for i in range(0, max_time):
                probe.step()
                if probe.hit_x:
                    vxs.append((vx, probe.time))
                # end early if you've crossed the target
                elif probe.left and probe.right:
                    break

        v0s = []
        # pair up vx and vy values that hit in the same amount of time
        for vx in vxs:
            for vy in vys:
                if vx[1] == vy[1]:
                    v0s.append((vx[0], vy[0]))

        # you'll get some dupes because some pairs stay in the target for a few
        # steps, so throw a set() on there
        return set(v0s)

    @staticmethod
    def _get_target(filename):
        with open(filename) as f:
            line = f.readline()
        xs = line[line.index("x=") + 2:line.index(",")].split("..")
        ys = line[line.index("y=") + 2:len(line)].split("..")
        return (int(xs[0]), int(ys[0])), (int(xs[1]), int(ys[1]))


# test on the example to ensure I'm doing this correctly
class Tests(TestCase):

    def test_max_height(self):
        pcheck = ProbeChecker("day17ex.txt")
        self.assertEqual(45, pcheck.max_height())

    def test_v0s(self):
        exv0s = []
        with open("day17exv0s.txt") as f:
            for line in f:
                parts = line.strip().split(" ")
                for part in parts:
                    if len(part) == 0:
                        continue
                    exv0s.append(tuple(int(p) for p in part.split(",")))

        pcheck = ProbeChecker("day17ex.txt")
        self.assertEqual(set(exv0s), pcheck.find_v0s())


if __name__ == "__main__":
    pcheck = ProbeChecker("day17.txt")
    print(pcheck.max_height())
    print(len(pcheck.find_v0s()))
