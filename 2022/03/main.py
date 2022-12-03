from collections import defaultdict
from itertools import islice


def get_score(item):

    val = ord(item) - ord("@")

    # uppercase
    if val <= 26:
        return val + 26
    # lowercase
    else:
        return ord(item) - ord("`")

class Rucksack():

    def __init__(self, line: str):

        self.compartments = []

        split = len(line) // 2
        self.compartments.append(self.get_items(line[:split]))
        self.compartments.append(self.get_items(line[split:]))

        self.items = self.get_items(line[:-1])


    @staticmethod
    def get_items(item_str: str):
        items = defaultdict(int)

        for c in item_str:
            items[c] += 1

        return items


    def get_dupe_score(self):
        dupes = set(self.compartments[0].keys()) & set(self.compartments[1].keys())

        assert len(dupes) == 1

        dupe = list(dupes)[0]

        return get_score(dupe)



class Group():

    def __init__(self, rucksacks: list[Rucksack]):
        assert len(rucksacks) == 3
        self.rucksacks = rucksacks


    def get_badge_score(self):

        dupes = (
            self.rucksacks[1].items.keys() &
            self.rucksacks[0].items.keys() &
            self.rucksacks[2].items.keys()
        )

        assert len(dupes) == 1

        dupe = list(dupes)[0]

        return get_score(dupe)


def parse_input():

    data = []
    with open("in.txt") as f:
        for line in f:
            data.append(Rucksack(line))
    return data


def part1(rucksacks):
    return sum([r.get_dupe_score() for r in rucksacks])


def part2(rucksacks):
    return sum([
        Group(p).get_badge_score() for p in
        [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
    ])
    


def main():

    rucksacks = parse_input()
    print(part1(rucksacks))
    print(part2(rucksacks))
    

main()
