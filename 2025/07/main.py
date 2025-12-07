from collections import defaultdict

def parse(name="input.txt"):
    splitters = set()

    with open(name) as f:
        for i, line in enumerate(f):
            for j, c in enumerate(line.strip()):
                match c:
                    case "S":
                        start = (i, j)
                    case "^":
                        splitters.add((i, j))
                    case _:
                        pass
    return start, splitters, i + 1



def step(beams: set, splitters: set, height: int):
    next_beams = list()
    splits = 0

    for beam in beams:
        new = (beam[0] + 1, beam[1])
        if new[0] == height:
            break
        elif new in splitters:
            next_beams.append((new[0], new[1] + 1))
            next_beams.append((new[0], new[1] - 1))
            splits += 1
        else:
            next_beams.append(new)

    return next_beams, splits


def part1(start, splitters, height):
    beams = set([start])
    total_splits = 0
    
    while beams:
        beams, splits = step(beams, splitters, height)
        total_splits += splits
        beams = set(beams)

    return total_splits


def visit_merge(*v):
    merged = dict(v[0])

    for b in v[1:]:
        for k in b.keys():
            if k not in merged:
                merged[k] = b[k]
            else:
                merged[k] += b[k]

    return merged


def part2_impl(start, splitters, height):
    visits = {start: 1}
    beams, _ = step(set([start]), splitters, height)
    if not beams:
        # reached the bottom
        return visits
    elif len(beams) == 1:
        # no split, keep going
        return visit_merge(visits, part2_impl(list(beams)[0], splitters, height))
    else:
        # we split!
        return visit_merge(visits, *[part2_impl(beam, splitters, height) for beam in beams])


def part2(start, splitters, height):
    visits = part2_impl(start, splitters, height)

    s = sum([v for k, v in visits.items() if k[0] == height - 1])
    return s


def part2_bfs(start, splitters, height):
    visit_count = defaultdict(int)
    visit_count[start] = 1
    queue = set([start])

    while queue:
        # sort the queue to ensure we process row-by-row
        ql = sorted(queue, key=lambda t: t[0])
        curr = ql.pop(0)
        queue.remove(curr)
        beams, _ = step(set([curr]), splitters, height)

        if not beams:
            # reached the bottom
            continue
        elif len(beams) == 1:
            # no split, keep going
            beam = beams.pop()
            queue.add(beam)
            visit_count[beam] += visit_count[curr]
        else:
            # we split! enqueue and count the next row
            for beam in beams:
                visit_count[beam] += visit_count[curr]
            queue.update(beams)

    # answer: count the visits on the bottom row
    return sum([v for k, v in visit_count.items() if k[0] == height - 1])


start, splitters, height = parse("ex_input.txt")
assert 21 == part1(start, splitters, height)
assert 40 == part2(start, splitters, height)
assert 40 == part2_bfs(start, splitters, height)

start, splitters, height = parse()
print(part1(start, splitters, height))
print(part2_bfs(start, splitters, height))

