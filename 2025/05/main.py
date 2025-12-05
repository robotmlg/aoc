
def parse(name="input.txt"):
    with open(name) as f:
        s = f.read()

    top, bottom = s.split("\n\n")

    ranges = []
    for r in top.split("\n"):
        a, b = r.strip().split("-")
        ranges.append((int(a), int(b)))

    return ranges, [int(i.strip()) for i in bottom.split("\n")]


def part1(fresh, ingredients):

    def is_fresh(fresh, ingredient):
        for r in fresh:
            if ingredient >= r[0] and ingredient <= r[1]:
                return True
        return False

    return sum([is_fresh(fresh, i) for i in ingredients])


def r_merge2(rs):
    # assume input list sorted by first key
    if len(rs) == 1:
        return rs

    # process the first two elements
    a = rs[0]
    b = rs[1]
    # new list contains merged range, if it's there
    # if the second range is fully contained
    if a[0] <= b[0] <= b[1] <= a[1]:
        return r_merge2([a] + rs[2:])
    # if the second range overlaps and extends
    elif a[0] <= b[0] <= a[1] <= b[1]:
        return r_merge2([(a[0], b[1])] + rs[2:])
    # else, they don't overlap
    else:
        # extract separate range, merge the rest
        return [a] + r_merge2(rs[1:])


def part2(fresh):
    # combine overlapping ranges
    s_fresh = sorted(fresh, key=lambda t: t[0])

    reduced = r_merge2(s_fresh)
            
    return sum([r[1] + 1 - r[0] for r in reduced])


fresh, ingredients = parse()
print(part1(fresh, ingredients))
print(part2(fresh)) 
