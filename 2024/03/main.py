import re


def parse():
    with open("input.txt", "r") as f:
        return f.read()


def part1(memory):
    muls = re.finditer(r"mul\((\d+),(\d+)\)", memory)
    return sum([int(m.group(1)) * int(m.group(2)) for m in muls])


def part2(memory):
    instructions = re.finditer(r"(mul|do|don't)(\((\d+),(\d+)\)|\(\))", memory)
    enabled = True
    total = 0
    for inst in instructions:
        match inst.group(1):
            case "do":
                enabled = True
            case "don't":
                enabled = False
            case "mul":
                if enabled:
                    total += int(inst.group(3)) * int(inst.group(4))
            case _:
                pass
    return total


memory = parse()
print(part1(memory))
print(part2(memory))

