import re


class Step():
    
    def __init__(self, cnt, fr, to):
        self.cnt = cnt
        self.fr = fr
        self.to = to


    def __str__(self):
        return f"move {self.cnt} from {self.fr} to {self.to}"


class Stacks():

    def __init__(self, lines):
        self.stacks = {int(n):[] for n in lines[-1].strip().split(" ") if len(n) > 0}
        
        indices = range(1, len(lines[0]), 4)
        for line in lines[-2::-1]:
            for crate in enumerate(indices):
                if line[crate[1]] != " ":
                    self.stacks[crate[0] + 1].append(line[crate[1]])


    def apply_step_part1(self, step: Step):
        for i in range(step.cnt):
            crate = self.stacks[step.fr].pop()
            self.stacks[step.to].append(crate)


    def apply_step_part2(self, step: Step):
        moving = self.stacks[step.fr][-step.cnt:]
        staying = self.stacks[step.fr][:-step.cnt]

        self.stacks[step.fr] = staying
        self.stacks[step.to].extend(moving)


    def get_top_crates(self):
        return [s[-1] for s in self.stacks.values()]


def parse_input():
    phase = "stacks"
    step_regex = re.compile("move (\d+) from (\d+) to (\d+)")

    stack_lines = []
    steps = []
    with open("in.txt") as f:
        for line in f:
            if phase == "stacks":
                if len(line) == 1:
                    phase = "steps"
                    stacks = Stacks(stack_lines)
                else:
                    stack_lines.append(line)
            elif phase == "steps":
                m = step_regex.match(line)
                steps.append(Step(int(m[1]), int(m[2]), int(m[3])))
            else:
                raise Exception

    return stacks, steps


def part1(stacks, steps):
    for step in steps:
        stacks.apply_step_part1(step)
    return "".join(stacks.get_top_crates())


def part2(stacks, steps):
    for step in steps:
        stacks.apply_step_part2(step)
    return "".join(stacks.get_top_crates())


def main():
    stacks, steps = parse_input()
    print(part1(stacks, steps))
    stacks, steps = parse_input()
    print(part2(stacks, steps))


main()
