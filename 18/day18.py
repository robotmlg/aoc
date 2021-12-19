from math import ceil, floor


def parse_number(line):
    out = []
    for c in line:
        if c in "[]":
            out.append(c)
        elif c.isdigit():
            # assumption: the input is always in reduced form and has only
            # digits
            out.append(int(c))
    return out


def reduce(x):
    n = list(x)
    # find anything to explode, then recurse
    depth = 0
    for i in range(len(n)):
        c = n[i]
        if depth >= 5 and type(c) is int and type(n[i + 1]) is int:
            left = c
            right = int(n[i + 1])

            # add left and right to previous and next values, respectively
            for j in range(i - 1, -1, -1):
                if type(n[j]) is int:
                    n[j] = n[j] + left
                    break
            for j in range(i + 2, len(n)):
                if type(n[j]) is int:
                    n[j] = n[j] + right
                    break
            # set current pair to 0
            reduced = n[:i - 1]
            reduced.append(0)
            reduced.extend(n[i + 3:])

            return reduce(reduced)
        elif c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
    # if there was nothing to explode, find anything to split
    for i in range(len(n)):
        c = n[i]
        if type(c) is int and c >= 10:
            new_pair = ["[", floor(c / 2), ceil(c / 2), "]"]
            reduced = n[:i]
            reduced.extend(new_pair)
            reduced.extend(n[i + 1:])
            return reduce(reduced)

    return n


def add(x, y):
    a = list(x)
    b = list(y)

    out = ["["]
    out.extend(a)
    out.extend(b)
    out.append("]")

    return reduce(out)


def magnitude(x):

    def compute(l, r):
        return 3 * l + 2 * r

    n = list(x)
    while len(n) > 1:
        for i in range(len(n)):
            if type(n[i]) is int and type(n[i + 1]) is int:
                m = n[:i - 1]
                m.append(compute(n[i], n[i + 1]))
                m.extend(n[i + 3:])
                n = m
                break

    return n[0]



def day18():
    number = []
    with open("day18.txt") as f:
        for line in f:
            new_number = parse_number(line)
            if number:
                number = add(number, new_number)
            else:
                number = new_number
    return magnitude(number)

if __name__ == "__main__":
    print(day18())
