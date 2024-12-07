import re
import itertools

def parse(file="input.txt"):
    output = []
    with open(file, "r") as f:
        for l in f:
            vals = re.split(r"[: ]", l)
            output.append({
                "goal": int(vals[0]),
                "operands": [int(v) for v in vals[2:]],
            })
    return output


part1_ops = {
    "*": lambda a, b: a * b,
    "+": lambda a, b: a + b,
}

part2_ops = {
    "*": lambda a, b: a * b,
    "+": lambda a, b: a + b,
    "||": lambda a, b: int(f"{a}{b}"),
}

def test(equation, operation_map):
    op_cnt = len(equation["operands"]) - 1
    to_test = itertools.product(operation_map.keys(), repeat=op_cnt)
    for ops in to_test:
        eq = [equation["operands"][0]] + [x for i in range(op_cnt) for x in [ops[i], equation["operands"][i+1]]]

        result = equation["operands"][0]
        for i in range(op_cnt):
            result = operation_map[ops[i]](result, equation["operands"][i+1])

        if equation["goal"] == result:
            return True

    return False


def test_all(equations, ops):
    return sum([
        equation["goal"]
        for equation in equations
        if test(equation, ops)
    ])


equations = parse()
print(test_all(equations, part1_ops))
print(test_all(equations, part2_ops))
            
