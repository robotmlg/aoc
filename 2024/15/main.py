
def parse(file="input.txt"):
    with open(file, "r") as f:
        data = f.read()
        grid_data, actions_data = data.split("\n\n")
        grid = [list(l.strip()) for l in grid_data.split("\n")]

        boxes = []
        walls = []
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                c = grid[y][x]
                match c:
                    case "#":
                        walls.append(complex(x, y))
                    case "O":
                        boxes.append(complex(x, y))
                    case "@":
                        robot = complex(x, y)
                    case ".":
                        pass
                    case _:
                        raise Exception("Invalid action!")

        actions = []
        for c in [c for l in actions_data for c in list(l.strip())]:
            match c:
                case "^":
                    actions.append(complex(0, -1))
                case ">":
                    actions.append(complex(1, 0))
                case "v":
                    actions.append(complex(0, 1))
                case "<":
                    actions.append(complex(-1, 0))
                case _:
                    raise Exception("Invalid action!")

        return {
            "robot": robot,
            "boxes": boxes,
            "walls": walls,
            "actions": actions,
            "width": len(grid[0]),
            "height": len(grid),
        }


def coordinate(box):
    return int(100 * box.imag + box.real)


def part1(state):

    robot = state["robot"]
    boxes = set(state["boxes"])

    def is_wall(p):
        return p in state["walls"]

    def is_box(p):
        return p in boxes

    def is_open(p):
        return not is_box(p) and not is_wall(p)

    for a in state["actions"]:
        # find the next open space in the action direction
        p = robot + a
        while not is_open(p) and not is_wall(p): 
            p += a
        if not is_wall(p) and is_open(p):
            boxes_to_push = set([ robot + a * i for i in range(1, int(((p - robot) / a).real))])
            boxes_to_add = set([b + a for b in boxes_to_push])

            boxes -= boxes_to_push
            boxes |= boxes_to_add

            robot += a

    return sum([coordinate(b) for b in boxes])


def part2(state):
    # wiiiiiide grid
    def widen(p):
        return (complex(2 * p.real, p.imag), complex(2 * p.real + 1, p.imag))

    robot = widen(state["robot"])[0]
    walls = [w2 for w in state["walls"] for w2 in widen(w)]
    boxes = {p : b for b in [widen(b) for b in state["boxes"]] for p in b}

    def is_wall(p):
        return p in walls

    def is_box(p):
        return p in boxes.keys()

    def is_open(p):
        return not is_box(p) and not is_wall(p)

    def can_move(robot, a):
        p = robot + a
        if is_open(p):
            return True, []
        elif is_wall(p):
            return False, []
        # there's a box
        if a.imag == 0:
            # if we're moving horizontally, just consider the far side of the box
            can_box_move, far_boxes = can_move(p + a, a)
            return can_box_move, far_boxes + [boxes[p]]
        # if we're moving vertically, consider any touching boxes
        can_box_move = True
        all_boxes = [boxes[p]]
        for b in boxes[p]:
            nc, nb = can_move(b, a)
            can_box_move &= nc
            all_boxes.extend(nb)
        return can_box_move, all_boxes

    for a in state["actions"]:
        # find the next open space in the action direction
        go, boxes_to_push = can_move(robot, a)
        if go:
            if boxes_to_push:
                keys_to_push = [k for b in boxes_to_push for k in b]
                boxes_to_add = { k + a: (boxes[k][0] + a, boxes[k][1] + a) for k in keys_to_push}

                for k in keys_to_push:
                    if k in boxes:
                        del boxes[k]
                boxes.update(boxes_to_add)

            robot += a

    return sum([coordinate(b[0]) for b in set(boxes.values())])


state = parse()
print(part1(state))
print(part2(state))

