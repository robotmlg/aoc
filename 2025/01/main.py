 
def sgn(x):
    return (x > 0) - (x < 0)


def parse(name="input.txt"):
    turns = []
    with open(name) as f:
        for l in f:
            direction = -1 if l[0] == "L" else 1
            n = direction * int(l[1:])
            turns.append(n)
    return turns


def part1(turns, start=50, size=100):
    zero_count = 0 if start != 0 else 1
    curr = start
    for t in turns:
        curr += t
        curr %= size
        if curr == 0:
            zero_count += 1

    return zero_count


def part2(turns, start=50, size=100):
    zero_count = 0
    curr = start
    for t in turns:
        full_rotations = abs(t) // size
        zero_count += full_rotations
        new_t = t - sgn(t) * size * full_rotations
        nxt = curr + new_t

        if (curr < size and nxt >= size) or (curr > 0 and nxt <= 0):
            zero_count += 1

        curr = nxt % size
        print(f"turn {t}: {zero_count}")

    return zero_count
    


turns = parse()
print(part1(turns))
print(part2(turns))
