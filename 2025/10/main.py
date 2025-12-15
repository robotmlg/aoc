from itertools import product


class Machine:
    def __init__(self, line):
        parts = line.strip().split(" ")

        self.lights_goal = [c == "#" for c in list(parts.pop(0))[1:-1]]

        self.joltage_goal = [int(n) for n in parts.pop(-1)[1:-1].split(",")]

        self.buttons = [self._parse_button(b, len(self.lights_goal)) for b in parts]

    def solve_indicators(self):
        for i in range(100):
            for pushes in product(self.buttons, repeat=i):
                test_lights = [False] * len(self.lights_goal)
                for push in pushes:
                    Machine.push_indicator_button(test_lights, push)

                if self.lights_goal == test_lights:
                    return pushes

    def solve_joltage(self):
        min_required = max(self.joltage_goal)
        for i in range(min_required, min_required * 2):
            print(f"solving {self.joltage_goal} for {i}")
            for pushes in product(self.buttons, repeat=i):
                test_joltage = [0] * len(self.joltage_goal)
                for push in pushes:
                    Machine.push_joltage_button(test_joltage, push)
                    if any([test_joltage[j] > self.joltage_goal[j] for j in range(len(test_joltage))]):
                        break

                if self.joltage_goal == test_joltage:
                    return pushes
        raise Exception(f"No result found for {self.joltage_goal}")

    @staticmethod
    def push_indicator_button(lights, button):
        for i in range(len(lights)):
            lights[i] ^= button[i]

    @staticmethod
    def push_joltage_button(joltages, button):
        for i in range(len(joltages)):
            joltages[i] += button[i]

    def __repr__(self):
        return f"{self.lights_goal} {self.buttons} {self.joltage}\n"

    @staticmethod
    def _parse_button(button_str: str, light_cnt: int):
        button = [False] * light_cnt
        for n in button_str[1:-1].split(","):
            button[int(n)] = True
        return button


def parse(name="input.txt"):
    machines = []

    with open(name) as f:
        for line in f:
            machines.append(Machine(line))

    return machines


def part1(machines):
    return sum([len(m.solve_indicators()) for m in machines])


def part2(machines):
    return sum([len(m.solve_joltage()) for m in machines])


machines = parse("ex_input.txt")
assert 7 == part1(machines)
print("part 1 ex passed")
assert 33 == part2(machines)
print("part 2 ex passed")

machines = parse()
print(part1(machines))
print(part2(machines))

