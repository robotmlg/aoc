
def parse(file="input.txt"):
    grid = []
    with open(file, "r") as f:
        for line in f:
            grid.append(list(line))
    # map the grid
    obstacles = set()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            match grid[row][col]:
                case "^":
                    pos, direction = complex(row, col), -1
                case ">":
                    pos, direction = complex(row, col), 1j
                case "v":
                    pos, direction = complex(row, col), 1
                case "<":
                    pos, direction = complex(row, col), -1j
                case "#":
                    obstacles.add(complex(row, col))
                case _:
                    pass
    return {
        "obstacles": obstacles,
        "start": pos,
        "direction": direction,
        "width": len(grid[0]),
        "height": len(grid),
    }


def walk(state, max_steps=50000):
    def is_in_grid(x):
        return 0 <= x.real < state["height"] and 0 <= x.imag < state["width"]
        
    visited = []
    pos = state["start"]
    direction = state["direction"]
    while is_in_grid(pos) and len(visited) < max_steps:
        visited.append(pos)
        next_pos = pos + direction
        # while loop to account for doing a u-turn on the spot
        while is_in_grid(next_pos) and next_pos in state["obstacles"]:
            direction = direction * -1j
            next_pos = pos + direction
        pos = next_pos

    if len(visited) == max_steps:
        return None

    return set(visited)


def part2(state, visited):
    possible_positions = set()
    for p in visited:
        # test every point along the path
        new_obstacles = set(state["obstacles"])
        new_obstacles.add(p)
        walk_result = walk({
            "obstacles": new_obstacles,
            "start": state["start"],
            "direction": state["direction"],
            "width": state["width"],
            "height": state["height"],
        }, max_steps=5*len(visited))

        if walk_result is None:
            possible_positions.add(p)

    return len(possible_positions)
    

state = parse()
visited = walk(state)
print(len(visited))
print(part2(state, visited))

