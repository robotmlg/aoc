
def parse():
    reports = []
    with open("input.txt", "r") as f:
        for l in f:
            reports.append([int(n) for n in l.split()])
    return reports


def is_report_safe(r):
    diffs = [r[i] - r[i-1] for i in range(1, len(r))]
    return (
        (all([d > 0 for d in diffs]) or all([d < 0 for d in diffs])) and
        all([1 <= abs(d) <= 3 for d in diffs])
    )


def part1(reports):
    return sum([int(is_report_safe(r)) for r in reports])


def part2(reports):
    total_safe = 0
    for r in reports:
        if is_report_safe(r):
            total_safe += 1
        else:
            # dampen
            for i in range(len(r)):
                r2 = list(r)
                r2.pop(i)
                if is_report_safe(r2):
                    total_safe += 1
                    break
                
    return total_safe


reports = parse()
print(part1(reports))
print(part2(reports))
