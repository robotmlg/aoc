

def parse_input():
    with open("in.txt") as f:
        for line in f:
            return line


def find_unique_len(datastream, length):
    last_n = []
    for i, c in enumerate(datastream):
        if len(last_n) < length:
            last_n.append(c)
        else:
            if len(set(last_n)) == length:
                return i
            last_n.append(c)
            last_n.pop(0)


def part1(datastream):
    return find_unique_len(datastream, 4)


def part2(datastream):
    return find_unique_len(datastream, 14)
            

def main():
    datastream = parse_input()
    print(part1(datastream))
    print(part2(datastream))


main()
