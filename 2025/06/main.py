import re

def compute(problem):
    op = problem.pop()
    loc = {}
    exec(f"res = {str(op.join(problem))}", globals(), loc)
    return int(loc["res"])


def part1(name="input.txt"):
    problems = []
    with open(name) as f:
        for line in f:
            line_shrunk = re.sub(r"\s+", " ", line.strip())
            parts = line_shrunk.split(" ")
            for i, p in enumerate(parts):
                if i >= len(problems):
                    problems.append([p])
                else:
                    problems[i].append(p)
    return sum([compute(p) for p in problems])


def part2(name="input.txt"):
    lines = []
    with open(name) as f:
        for line in f:
            lines.append(line)

    problems = []

    problem = []
    # iterate right to left
    for i in range(len(lines[0]) - 2, -1, -1):
        val = ""
        for line_j in range(0, len(lines)):
            char = lines[line_j][i]
            if char.isdigit():
                val += char
            if char in ["*", "+"]:
                problem.append(val)
                problem.append(char)
                problems.append(problem)
                problem = []
                break
        else:
            if val:
                problem.append(val)

    return sum([compute(p) for p in problems])


print(part1())
print(part2())
