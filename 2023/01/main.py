import re

part_one_regex = re.compile(r"\d")

def first_digit(s):
    match = part_one_regex.search(s)
    return int(match.group(0))

def last_digit(s):
    return first_digit(s[::-1])

numbers_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = "|".join(numbers_list)

def first_digit_2(s):
    match = re.search(fr"(\d|{numbers})", s)
    num = match.group(0)

    if len(num) == 1:
        return int(num)
    return numbers_list.index(num)

def last_digit_2(s):
    match = re.search(fr"(\d|{numbers[::-1]})", s[::-1])
    num = match.group(0)

    if len(num) == 1:
        return int(num)
    return numbers_list.index(num[::-1])

def part1():
    sum = 0
    with open("pt1.txt") as f:
        for l in f:
            val = first_digit(l) * 10 + last_digit(l)
            sum += val

    print(sum)

def part2():
    sum = 0
    with open("pt1.txt") as f:
        for l in f:
            val = first_digit_2(l) * 10 + last_digit_2(l)
            sum += val

    print(sum)

part1()
part2()
