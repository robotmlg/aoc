
class Cave:
    
    def __init__(self, name: str):
        self.name = name
        self.visited = False
        self.neighbors = []
        self.cant_visit = ["start", "end"]

    def visit(self):
        self.visited = True

    def unvisit(self):
        self.visited = False

    def can_visit(self):
        return self._is_big() or (not self.visited and self._is_small())

    def add_neighbor(self, c):
        self.neighbors.append(c)

    def valid_neighbors(self, can_double_visit=False):
        valid = []
        # big
        valid.extend([n for n in self.neighbors if n._is_big()])

        if not can_double_visit:
            # unvisited small
            valid.extend([n for n in self.neighbors if n._is_small() and n.name not in self.cant_visit and n.can_visit()])
        else:
            # all small
            valid.extend([n for n in self.neighbors if n._is_small() and n.name not in self.cant_visit])


        return sorted(set(valid))

    def has_end_path(self):
        return len([n for n in self.neighbors if n.name == "end"]) == 1

    def _is_small(self):
        return self.name[0].islower()

    def _is_big(self):
        return not self._is_small()

    def __lt__(self, other):
        return self.name < other.name


class CaveSystem:

    def __init__(self):
        caves = {}

        with open("day12.txt") as f:
            for line in f:
                new_caves = line.strip().split("-")
                for new_name in new_caves:
                    if new_name not in caves.keys():
                        caves[new_name] = Cave(new_name)

                caves[new_caves[0]].add_neighbor(caves[new_caves[1]])
                caves[new_caves[1]].add_neighbor(caves[new_caves[0]])

        self.start = caves["start"]

    def count_paths(self, cave=None, previous=None, can_double_visit=False):
        if cave is None:
            cave = self.start

        if previous is None:
            previous = []

        # if you have already double visited, cancel
        if cave._is_small() and cave.name in previous:
          if not can_double_visit:
            # really should never end up in this case, because we shouldn't even
            # attempt to do a double visit, but I'm fine with this hack
            return 0
          can_double_visit = False

        previous.append(cave.name)
        paths = 0

        if cave.has_end_path():
            paths += 1

        cave.visit()

        next_neighbors = cave.valid_neighbors(can_double_visit)

        for c in next_neighbors:
            paths += self.count_paths(c, list(previous), can_double_visit)

        cave.unvisit()

        return paths 
              

def day12A():
    return CaveSystem().count_paths()


def day12B():
    return CaveSystem().count_paths(can_double_visit=True)


if __name__ == "__main__":
    print(day12A())
    print(day12B())
