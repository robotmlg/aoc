
def parse_input():
    forest = []
    with open("in.txt") as f:
        for line in f:
            forest.append([int(t) for t in list(line[:-1])])

    return forest


def part1(forest):
    visible = [
        [False for _ in forest[0]] for _ in forest
    ]

    # north view
    for j in range(0, len(forest[0])):
        tallest = -1
        for i in range(0, len(forest)):
            if forest[i][j] > tallest:
                visible[i][j] = True
                tallest = forest[i][j]
    # east
    for i in range(0, len(forest)):
        tallest = -1
        for j in range(0, len(forest[i])):
            if forest[i][j] > tallest:
                visible[i][j] = True
                tallest = forest[i][j]
    # south
    for j in range(0, len(forest[0])):
        tallest = -1
        for i in range(len(forest) - 1, -1, -1):
            if forest[i][j] > tallest:
                visible[i][j] = True
                tallest = forest[i][j]
    # west
    for i in range(0, len(forest)):
        tallest = -1
        for j in range(len(forest[i]) - 1, -1, -1):
            if forest[i][j] > tallest:
                visible[i][j] = True
                tallest = forest[i][j]

    return sum([v_row.count(True) for v_row in visible])


def part2(forest):
    all_scenic = [
        [0 for _ in forest[0]] for _ in forest
    ]

    for i in range(0, len(forest)):
        for j in range(0, len(forest[i])):
            scenic = 1

            # north
            curr = 0
            if i != 0:
                k = i - 1
                while k >= 0:
                    if forest[k][j] < forest[i][j]:
                        curr += 1
                    else:
                        curr += 1
                        break
                    k -= 1

            scenic *= curr

            # east
            curr = 0
            if j != len(forest[i]) - 1:
                k = j + 1
                while k <= len(forest[i]) - 1:
                    if forest[i][k] < forest[i][j]:
                        curr += 1
                    else:
                        curr += 1
                        break
                    k += 1
            scenic *= curr

            # south
            curr = 0
            if i != len(forest) - 1:
                k = i + 1
                while k <= len(forest) - 1:
                    if forest[k][j] < forest[i][j]:
                        curr += 1
                    else:
                        curr += 1
                        break
                    k += 1
            scenic *= curr

            # west
            curr = 0
            if j != 0:
                k = j - 1
                while k >= 0:
                    if forest[i][k] < forest[i][j]:
                        curr += 1
                    else:
                        curr += 1
                        break
                    k -= 1
            scenic *= curr

            all_scenic[i][j] = scenic

           #  break
        # break

    for row in all_scenic:
        print(row)
    return max([max(row) for row in all_scenic])


def main():
    forest = parse_input()
    print(part1(forest))
    print(part2(forest))

main()
