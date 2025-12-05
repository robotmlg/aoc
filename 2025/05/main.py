
def parse(name="input.txt"):
    with open(name) as f:
        s = f.read()

    top, bottom = s.split("\n\n")

    ranges = []
    for r in top.split("\n"):
        a, b = r.strip().split("-")
        ranges.append(range(int(a), int(b) + 1))

    return ranges, [int(i.strip()) for i in bottom.split("\n")]


def part1(fresh, ingredients):

    def is_fresh(fresh, ingredient):
        for r in fresh:
            if ingredient in r:
                return True
        return False

    return sum([is_fresh(fresh, i) for i in ingredients])


def part2(fresh):
    # combine overlapping ranges
    return sum([len(r) for r in reduced])


fresh, ingredients = parse("ex_input.txt")
print(part1(fresh, ingredients))
print(part2(fresh)) 
