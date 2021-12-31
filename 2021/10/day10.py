from functools import reduce

brackets = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


scores = {
   ")": 1,
   "]": 2,
   "}": 3,
   ">": 4,
}


def score_corrupt_line(line):
    stack = []
    for char in line:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if brackets[stack.pop()] != char:
                if char == ")":
                    return 3
                elif char == "]":
                    return 57
                elif char == "}":
                    return 1197
                elif char == ">":
                    return 25137
        else:
            raise Exception(f"Unknown character {char}!")
    # incomplete line, ignore
    return 0


def score_incomplete_line(line):
    stack = []
    for char in line:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if brackets[stack.pop()] != char:
                # corrupt line, ignore
                return 0
        else:
            raise Exception(f"Unknown character {char}!")
    stack.reverse()
    return reduce(lambda total, character: total * 5 + scores[brackets[character]],
                  stack, 0)


def day10A():
    with open("day10.txt") as f:
        return sum([score_corrupt_line(line.strip()) for line in f])


def day10B():
    with open("day10.txt") as f:
        scores = sorted(filter(lambda x: x != 0,
                               [score_incomplete_line(line.strip()) for line in f]))
        return scores[(len(scores) - 1) // 2]


if __name__ == "__main__":
    print(day10A())
    print(day10B())
