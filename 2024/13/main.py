import re

def parse(file="input.txt"):
    with open(file, "r") as f:
        data = f.read()
        matches = re.finditer(r"Button A: X([+-][0-9]+), Y([+-][0-9]+)\s+Button B: X([+-][0-9]+), Y([+-][0-9]+)\s+Prize: X=(\d+), Y=(\d+)", data)

        return [
            {
                "A": (int(m[1]), int(m[2])),
                "B": (int(m[3]), int(m[4])),
                "prize": (int(m[5]), int(m[6])),
            }
            for m in matches
        ]

def solve_machine(machine):
    x_a, y_a = machine["A"]
    x_b, y_b = machine["B"]
    p_x, p_y = machine["prize"]

    # apply Cramer's rule
    det = int(x_a * y_b - x_b * y_a)
    if det == 0:
        return 0
    a_presses = int(p_x * y_b - x_b * p_y) / det
    b_presses = int(x_a * p_y - p_x * y_a) / det

    if a_presses.is_integer() and b_presses.is_integer():
        return int(3 * a_presses + b_presses)
    return 0


machines = parse()
print(sum([
    solve_machine(m)
    for m in machines
]))
print(sum([
    solve_machine({
        "A": m["A"],
        "B": m["B"],
        "prize": (m["prize"][0] + 10000000000000, m["prize"][1] + 10000000000000),
    })
    for m in machines
]))

