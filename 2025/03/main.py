
def parse(name="input.txt"):
    banks = []
    with open(name) as f:
        for line in f:
            banks.append([int(b) for b in list(line.strip())])
    return banks


def jolt(bank, length):
    digits = []

    max_digit_index = -1
    for i in range(length):
        start_range = max_digit_index + 1
        end_range = len(bank) - (length - i) + 1

        max_digit = max(bank[start_range : end_range])
        max_digit_index = bank.index(max_digit, start_range if start_range < len(bank) - 2 else len(bank) - 2)

        digits.append(max_digit)

    return int("".join([str(d) for d in digits]))


def jolts(banks, length):
    return [jolt(b, length) for b in banks]


def part1(banks):
    return sum(jolts(banks, 2))


def part2(banks):
    return sum(jolts(banks, 12))
    

banks = parse()
print(part1(banks))
print(part2(banks))
