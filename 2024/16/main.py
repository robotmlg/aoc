import heapq
import sys

class Node:
    
    def __init__(self, i, j):
        self.point = complex(i, j)
        self.neighbors = set()

    def __repr__(self):
        return f"{self.point} -> {[n.point for n in self.neighbors]}"

    def __lt__(self, other):
        return self.point.real < other.point.real and self.point.imag < other.point.imag


class Maze:
    
    def __init__(self):
        self.nodes = dict()
        self.start = None
        self.end = None

    def add_node(self, i, j):
        n = Node(i, j)
        self.nodes[n.point] = n
        
        # check for neighbors
        for d in [1, -1, 1j, -1j]:
            curr = n.point + d
            if curr in self.nodes:
                self.nodes[curr].neighbors.add(n)
                n.neighbors.add(self.nodes[curr])

        return n

    def solve(self):

        dist = {}
        prev = {}
        queue = []
        for n in self.nodes.values():
            dist[n.point] = sys.maxsize
            prev[n.point] = None
            if n == self.start:
                heapq.heappush(queue, (0, n, complex(1, 0)))
            else:
                heapq.heappush(queue, (sys.maxsize, n, None))

        while queue:
            u = heapq.heappop(q)

            for n 


        return visits[self.end.point].score


def parse(file="input.txt"):
    with open(file, "r") as f:
        grid = [list(l.strip()) for l in f]

    maze = Maze()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            match grid[i][j]:
                case "#":
                    pass
                case ".":
                    maze.add_node(i, j)
                case "S":
                    n = maze.add_node(i, j)
                    maze.start = n
                case "E":
                    n = maze.add_node(i, j)
                    maze.end = n
                case c:
                    raise Exception(f"Invalid maze character {c}")

    return maze
        

maze = parse("testin.txt")
print(maze.solve())

