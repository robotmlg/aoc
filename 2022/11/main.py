from functools import reduce
from operator import mul

class Monkey():
    
    def __init__(self, lines: list[str]):
        self.id = int(lines[0].strip().split(" ")[1][:-1])
        self.items = [int(n.strip(",")) for n in lines[1].strip().split(" ")[2:]]
        self.op = " ".join(lines[2].strip().split(" ")[3:])

        # we only support divisibility tests
        assert lines[3].strip().split(" ")[1] == "divisible"
        self.divisibility = int(lines[3].strip().split(" ")[-1])
        assert lines[4].strip().split(" ")[1] == "true:"
        assert lines[5].strip().split(" ")[1] == "false:"
        self.pass_dest = int(lines[4].strip().split(" ")[-1])
        self.fail_dest = int(lines[5].strip().split(" ")[-1])
        self.inspections = 0

    def __str__(self):
        return f"""Monkey {self.id}: {self.items}"""

    def inspect(self):
        self.inspections += 1


def parse_input():
    monkeys = []
    with open("in.txt") as f:
        curr_lines = []
        for line in f:
            if line == "\n":
                monkeys.append(Monkey(curr_lines))
                curr_lines = []
            else:
                curr_lines.append(line)
        monkeys.append(Monkey(curr_lines))
    return monkeys


def solve(monkeys, rounds, divide):
    modulo_base = reduce(mul, [m.divisibility for m in monkeys])
    for i in range(0,rounds):
        for monkey in monkeys:
            # print(f"Monkey {monkey.id}:")
            while len(monkey.items):
                monkey.inspect()
                old = monkey.items.pop(0)
                # print(f"  Monkey inspects an item with a worry level of {old}")
                new = eval(monkey.op)
                # print(f"    Worry level is '{monkey.op}' to {new}")
                # print(f"    Monkey gets bored with item.  Worry leve is divided by 3 to {new//3}")
                if divide != 1:
                    new //= divide
                else:
                    new %= modulo_base
                    if new == 0:
                        new = modulo_base
                if new % monkey.divisibility == 0:
                    # print(f"    Current worry level is divisible by {monkey.divisibility}")
                    # print(f"    Item with worry level {new} is thrown to monkey {monkey.pass_dest}")
                    monkeys[monkey.pass_dest].items.append(new)
                else:
                    # print(f"    Current worry level is not divisible by {monkey.divisibility}")
                    # print(f"    Item with worry level {new} is thrown to monkey {monkey.fail_dest}")
                    monkeys[monkey.fail_dest].items.append(new)
    sorted_monkeys = sorted(monkeys, key=lambda x: x.inspections, reverse=True)
    return sorted_monkeys[0].inspections * sorted_monkeys[1].inspections


def main():
    monkeys = parse_input()
    print(solve(monkeys, 20, 3))
    monkeys = parse_input()
    print(solve(monkeys, 10000, 1))


main()
