class Node():

    def __init__(self, height: int, x: int, y: int):
        self.loc = (x, y)
        self.height = height
        self.neighbors = []
        self.visited = False
        self.parent = None

    def __str__(self):
        return f"{self.loc}: {self.height}: {[(v.loc, v.height) for v in self.neighbors]}"


    def add_neighbor(self, n):
        self.neighbors.append(n)

    def visit(self):
        self.visited = True

    def set_parent(self, p):
        self.parent = p


def part1():
    nodes = []
    root = None
    goal = None
    with open("in.txt") as f:
        for i, line in enumerate(f):
            nodes.append([])
            for j, c in enumerate(list(line.strip())):
                match c:
                    case "S":
                        root = Node(0, i, j)
                        nodes[-1].append(root)
                    case "E":
                        goal = Node(25, i, j)
                        nodes[-1].append(goal)
                    case x:
                        nodes[-1].append(Node(ord(x) - ord("a"), i, j))
    # populate neighbor relationships
    for i in range(len(nodes)):
        for j in range(len(nodes[i])):
            if i - 1 >= 0 and (nodes[i-1][j].height - nodes[i][j].height) <= 1:
                nodes[i][j].add_neighbor(nodes[i-1][j])

            if j - 1 >= 0 and (nodes[i][j-1].height - nodes[i][j].height) <= 1:
                nodes[i][j].add_neighbor(nodes[i][j-1])
                
            if i + 1 < len(nodes) and (nodes[i+1][j].height - nodes[i][j].height) <= 1:
                nodes[i][j].add_neighbor(nodes[i+1][j])

            if j + 1 < len(nodes[i]) and (nodes[i][j+1].height - nodes[i][j].height) <= 1:
                nodes[i][j].add_neighbor(nodes[i][j+1])

    queue = []
    root.visit()
    queue.append(root)

    while len(queue) > 0:
        v = queue.pop(0)

        if v is goal:
            length = 0
            curr = v
            while curr is not None:
                length += 1
                curr = curr.parent
            return length - 1

        for w in v.neighbors:
            if not w.visited:
                w.visit()
                w.set_parent(v)
                queue.append(w)


def part2():
    nodes = []
    root = None
    with open("in.txt") as f:
        for i, line in enumerate(f):
            nodes.append([])
            for j, c in enumerate(list(line.strip())):
                match c:
                    case "S":
                        x = Node(0, i, j)
                        nodes[-1].append(x)
                    case "E":
                        root = Node(25, i, j)
                        nodes[-1].append(root)
                    case x:
                        nodes[-1].append(Node(ord(x) - ord("a"), i, j))
    # populate neighbor relationships
    for i in range(len(nodes)):
        for j in range(len(nodes[i])):
            if i - 1 >= 0 and (nodes[i-1][j].height - nodes[i][j].height) >= -1:
                nodes[i][j].add_neighbor(nodes[i-1][j])

            if j - 1 >= 0 and (nodes[i][j-1].height - nodes[i][j].height) >= -1:
                nodes[i][j].add_neighbor(nodes[i][j-1])
                
            if i + 1 < len(nodes) and (nodes[i+1][j].height - nodes[i][j].height) >= -1:
                nodes[i][j].add_neighbor(nodes[i+1][j])

            if j + 1 < len(nodes[i]) and (nodes[i][j+1].height - nodes[i][j].height) >= -1:
                nodes[i][j].add_neighbor(nodes[i][j+1])

    queue = []
    root.visit()
    queue.append(root)

    while len(queue) > 0:
        v = queue.pop(0)

        if v.height == 0:
            length = 0
            curr = v
            while curr is not None:
                length += 1
                curr = curr.parent
            return length - 1

        for w in v.neighbors:
            if not w.visited:
                w.visit()
                w.set_parent(v)
                queue.append(w)


def main():
    print(part1())
    print(part2())


main()
