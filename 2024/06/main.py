

def parse(file="input.txt"):
    grid = []
    with open(file, "r") as f:
        for line in f:
            grid.append(list(line))
    # find the guard
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            match grid[row][col]:
                case "^":
                    return grid, (row, col), (-1, 0)  
                case ">":
                    return grid, (row, col), (0, 1)  
                case "v":
                    return grid, (row, col), (1, 0)  
                case "<":
                    return grid, (row, col), (0, -1)  
                case _:
                    pass
    raise Exception("Invalid input!")


def get_next_direction(direction):
    match direction:
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)
        case _:
            raise Exception(f"Invalid direction! {direction}")


def vector_add(a, b):
    return a[0] + b[0], a[1] + b[1]
    

def walk(grid, pos, direction):
    visited = set()
    obstacles = set()
    while 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[pos[0]]):
        visited.add(pos)
        next_pos = vector_add(pos, direction)
        if 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[pos[0]]) and grid[next_pos[0]][next_pos[1]] == "#":
            obstacles.add(next_pos)
            direction = get_next_direction(direction)
            next_pos = vector_add(pos, direction)
        pos = next_pos

    return visited, obstacles


def part2(grid, pos, direction):
    visited = []
    new_obstacles = set()
    while 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[pos[0]]):
        if pos in visited:
            print(f"previously visited {pos}")
            # we've been here before, check if we made a rectangle
            last_visit_idx = visited.index(pos)
            sub_path = visited[last_visit_idx:]
            # check if the sub path is a rectangle
            sub_direction = get_next_direction(direction)


        visited.append(pos)
        next_pos = vector_add(pos, direction)
        if 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[pos[0]]) and grid[next_pos[0]][next_pos[1]] == "#":
            direction = get_next_direction(direction)
            next_pos = vector_add(pos, direction)
        pos = next_pos

    return len(new_obstacles)


grid, start, direction = parse()
visited, obstacles = walk(grid, start, direction)
print(len(visited))
print(part2(grid, start, direction))
