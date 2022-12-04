import re


PAIR_REGEX = re.compile("(\d+)-(\d+),(\d+)-(\d+)")


class Pair():

    def __init__(self, line: str):
        m = PAIR_REGEX.match(line)

        self.assignment1 = (int(m[1]), int(m[2]))
        self.assignment2 = (int(m[3]), int(m[4]))

        assert self.assignment1[0] <= self.assignment1[1]
        assert self.assignment2[0] <= self.assignment2[1]


    def __str__(self):
        return str(self.assignment1) + "," + str(self.assignment2)


    def do_contain(self) -> bool:
        return (
            (self.assignment1[0] <= self.assignment2[0] and self.assignment2[1] <= self.assignment1[1]) or
            (self.assignment2[0] <= self.assignment1[0] and self.assignment1[1] <= self.assignment2[1])
        )


    def do_overlap(self) -> bool:
        return (
            self.assignment1[0] <= self.assignment2[0] <= self.assignment1[1] or
            self.assignment2[0] <= self.assignment1[0] <= self.assignment2[1] or
            self.assignment1[0] <= self.assignment2[1] <= self.assignment1[1] or
            self.assignment2[0] <= self.assignment1[1] <= self.assignment2[1]
        )



def parse_input():
    pairs = []
    with open("in.txt") as f:
        for line in f:
            pairs.append(Pair(line))

    return pairs


def part1(pairs):
    return [p.do_contain() for p in pairs].count(True)


def part2(pairs):
    return [p.do_overlap() for p in pairs].count(True)


def main():
    pairs = parse_input()
    print(part1(pairs))
    print(part2(pairs))


main()
