import re
import math

def parse(file="input.txt"):
    with open(file, "r") as f:
        matches = re.finditer(r"\bp=(\d+),(\d+) v=([0-9-]+),([0-9-]+)\b", f.read())
        return [
            {
                "p": complex(int(m[1]), int(m[2])),
                "v": complex(int(m[3]), int(m[4])),
            }
            for m in matches
        ]


def simulate(r, width, height, steps):
    p, v = r["p"], r["v"]
    x = (p.real + v.real * steps) % width
    y = (p.imag + v.imag * steps) % height
    return {"p": complex(x, y), "v": v}


def part1(robots, width, height):
    final = [simulate(r, width, height, 100)["p"] for r in robots]

    # split to quadrants
    quadrants = [[],[],[],[]]

    mid_w = width // 2
    mid_h = height // 2

    for p in final:
        if p.real == mid_w or p.imag == mid_h:
            continue
        elif p.real < mid_w and p.imag < mid_h:
            quadrants[0].append(p)
        elif p.real > mid_w and p.imag < mid_h:
            quadrants[1].append(p)
        elif p.real < mid_w and p.imag > mid_h:
            quadrants[2].append(p)
        elif p.real > mid_w and p.imag > mid_h:
            quadrants[3].append(p)

    return math.prod([len(q) for q in quadrants])

def part2(robots, width, height):
    for i in range(0, 100000):
        curr = [simulate(r, width, height, i)["p"] for r in robots]

        grid = []
        for h in range(height):
            grid.append([" " for _ in range(width)])
            
        for c in curr:
            grid[int(c.imag)][int(c.real)] = "X"
        grid_str = "\n".join(["".join(row) for row in grid])

        # find candidates
        if "XXXXXXXXX" in grid_str:
            print(grid_str)
            return i


robots = parse()
width, height = 101, 103
print(part1(robots, width, height))
print(part2(robots, width, height))
