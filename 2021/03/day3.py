from functools import reduce


def day3A():
    counts = []
    with open("day3.txt") as f:
        for line in f:
            line = line.strip()
            if len(counts) == 0:
                for _ in line:
                    counts.append([0, 0])
            val = int(line, 2)

            for i in range(0, len(line)):
                bit = 1 if (val & (1 << i)) > 0 else 0
                counts[i][bit] += 1

    gamma = reduce(lambda x, y: x ^ (y[1] << y[0]),
                   enumerate(map(lambda x: 0 if x[0] > x[1] else 1, counts)),
                   0)
    epsilon = reduce(lambda x, y: x ^ (y[1] << y[0]),
                     enumerate(map(lambda x: 0 if x[0] < x[1] else 1, counts)),
                     0)
    return gamma * epsilon


def criteria_filter(data, width, criterion):
    filtered_data = data
    for w in range(width - 1, -1, -1):
        mask = 1 << w
        bits = [0, 0]
        for d in filtered_data:
            bits[1 if (d & mask) > 0 else 0] += 1
        keep_bit = criterion(bits)
        filtered_data = [d for d in filtered_data
                         if keep_bit == (1 if (d & mask) > 0 else 0)]
        if len(filtered_data) == 1:
            return filtered_data[0]
    return 0


def day3B():
    lines = [line.strip() for line in open("day3.txt").readlines()]
    width = len(lines[0])
    nums = [int(line, 2) for line in lines]

    oxygen = criteria_filter(nums, width, lambda x: 1 if x[1] >= x[0] else 0)
    co2 = criteria_filter(nums, width, lambda x: 0 if x[0] <= x[1] else 1)

    return oxygen * co2


if __name__ == '__main__':
    print(day3A())
    print(day3B())
