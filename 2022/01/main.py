
def main():
    totals = []
    with open("pt1.txt") as f:
        current_total = 0
        for line in f:
            if line == "\n":
                totals.append(current_total)
                current_total = 0
            else:
                current_total += int(line)

    sorted_wts = sorted(totals)

    print(sorted_wts[-1])
    print(sum(sorted_wts[-3:]))


main()
