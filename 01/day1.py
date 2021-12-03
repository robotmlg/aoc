import sys


def day1(window=1):
    """for part 2, window = 3"""
    inc_cnt = 0
    sums = []
    last_val = sys.maxsize
    with open("day1.txt") as f:
        for line in f:
            val = int(line)
            sums = list(map(lambda x: x + val, sums))
            sums.append(val)
            if len(sums) < window:
                continue
            if last_val < sums[0]:
                inc_cnt += 1
            last_val = sums[0]
            sums.pop(0)

    print(inc_cnt)


if __name__ == '__main__':
    day1(3)

