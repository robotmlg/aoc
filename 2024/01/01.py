from collections import Counter


def parse_input():
    left = []
    right = []
    with open("input.txt", "r") as f:
        for l in f:
            lids = list(map(int, l.split()))
            left.append(lids[0])
            right.append(lids[1])

    return left, right
    

def part1(left, right):

    l_sort = sorted(left)
    r_sort = sorted(right)

    total_diff = 0

    for i in range(len(l_sort)):
        total_diff += abs(l_sort[i] - r_sort[i])

    return total_diff


def part2(left, right):
    l_count = Counter(left)
    r_count = Counter(right)

    similarity = 0
    for i in l_count.keys():
        if i in r_count.keys():
            similarity += i * r_count[i]
        
    return similarity


left, right = parse_input()
print(part1(left, right))
print(part2(left, right))
