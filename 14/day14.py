from collections import Counter, defaultdict


class Polymer:

    def __init__(self):
        with open("day14.txt") as f:
            polymer = f.readline().strip()
            self.counts = defaultdict(int, Counter(polymer))
            self.pairs = defaultdict(int,
                                     Counter(polymer[i:i + 2] for i in range(
                                             len(polymer) - 1)))
            f.readline()  # skip blank

            self.rules = {}
            for line in f:
                parts = line.strip().split(" ")
                self.rules[parts[0]] = parts[2]


    def step(self, steps=1):
        for _ in range(steps):
            new_pairs = self.pairs.copy()
            for p, cnt in self.pairs.items():
                to_insert = self.rules[p]
                self.counts[to_insert] += cnt

                left_pair = p[0] + to_insert
                right_pair = to_insert + p[1]
                new_pairs[left_pair] += cnt
                new_pairs[right_pair] += cnt
                new_pairs[p] -= cnt
                if new_pairs[p] <= 0:
                    del new_pairs[p]

            self.pairs = new_pairs

    @property
    def most_common_count(self):
        return Counter(self.counts).most_common()[0][1]

    @property
    def least_common_count(self):
        return Counter(self.counts).most_common()[-1][1]


if __name__ == "__main__":
    p = Polymer()
    p.step(10)
    print(p.most_common_count - p.least_common_count)
    p.step(30)
    print(p.most_common_count - p.least_common_count)
