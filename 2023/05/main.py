import re

class AlmanacMapEntry:
    
    def __init__(self, line):
        self.d_rng_start, self.s_rng_start, self.rng_len = [int(n) for n in line.split(" ")]
        self.s_rng = range(self.s_rng_start, self.s_rng_start + self.rng_len)

    def map_input(self, i):
        # print(f"mapping {i} on entry {self.d_rng_start} {self.s_rng_start} {self.rng_len}")
        if i in self.s_rng:
            return self.d_rng_start + (i - self.s_rng_start)
        return None

    def map_range(self, r):
        out_rng

        return out_rng, unmapped_rngs

class AlmanacMap:

    def __init__(self, s_name, d_name, es):
        self.s_name = s_name
        self.d_name = d_name
        self.entries = es

    def map_input(self, i):
        for e in self.entries:
            out = e.map_input(i)
            if out is not None:
                # print(f"{self.s_name} {i} maps to {self.d_name} {out}")
                return out
        # print(f"{self.s_name} {i} maps to {self.d_name} None")
        return i

    def map_range(self, r):
        for e in self.entries:
            out = e.map_range(r)
            if out is not None:
                return out
        return None


class Almanac:

    def __init__(self, s, ms):
        self.seeds = s
        self.maps = ms

    def map_input(self, i):
        curr = i
        for m in self.maps:
            # print(f"mapping {curr}")
            curr = m.map_input(curr)
            if curr is None:
                return None
        return curr

    def map_range(self, r):
        curr = r
        for m in self.maps:
            curr = m.map_range(curr)
            if curr is None:
                return None
        return curr

    def part1(self):
        dests = [self.map_input(s) for s in self.seeds]
        return min([d for d in dests if d is not None])

    def part2(self):
        seed_ranges = [(self.seeds[i], self.seeds[i+1]) for i in range(0, len(self.seeds), 2)]
        dest_ranges = [self.map_range(sr) for sr in seed_ranges]
        return(dest_ranges)

def parse_input():
    with open("in.txt", "r") as f:
        content = f.readlines()

    seeds = [int(n) for n in content[0][7:].split(" ")]

    maps = []
    i = 2
    while i < len(content):
        entries = []
        parsed_title = re.match(r"(\w+)-to-(\w+) map\:", content[i])
        s_name = parsed_title.group(1)
        d_name = parsed_title.group(2)
        j = i + 1
        while j < len(content) and len(content[j].strip()) > 0:
            entries.append(AlmanacMapEntry(content[j]))

            j += 1

        maps.append(AlmanacMap(s_name, d_name, entries))
        i = j + 1

    return Almanac(seeds, maps)

almanac = parse_input()
print(almanac.part1())
print(almanac.part2())
