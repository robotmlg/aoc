import re


def parse(name="input.txt"):
    with open(name) as f:
        line = f.readline()

    ranges = [r.split("-") for r in line.split(",")]

    return [(int(r[0]), int(r[1])) for r in ranges]


def find_matches(ranges, regex):
    invalid_ids = []

    for r in ranges:
        for i in range(r[0], r[1] + 1):
            i_str = str(i)
            digits = len(i_str)

            if re.fullmatch(regex,  i_str):
                invalid_ids.append(i)

    return sum(invalid_ids)


def part1(ranges):
    return find_matches(ranges, r'^(.+)\1$')


def part2(ranges):
    return find_matches(ranges, r'^(.+)\1{1,}$')


ranges = parse()
print(part1(ranges))
print(part2(ranges))

