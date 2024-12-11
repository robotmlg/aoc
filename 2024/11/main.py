import functools

def parse(file="input.txt"):
    with open(file, "r") as f:
        return [int(n) for n in f.read().strip().split()]


@functools.cache
def transform(stone: int, n: int = 1) -> list[int]:
    #print(f"MISS {stone}")
    if stone == 0:
        ret = [1]
    elif len(str(stone)) % 2 == 0:
        string = str(stone)
        halfway = len(string) // 2
        left = string[:halfway]
        right = string[halfway:]
        ret = [int(left), int(right)]
    else:
        ret = [stone * 2024]

    if n == 1:
        return ret
    return [t for s in ret for t in transform(s, n-1)]


@functools.cache
def transform_count(stone, n: int = 0) -> int:
    if n == 0:
        return 1
    if stone == 0:
        return transform_count(1, n - 1)
    elif len(str(stone)) % 2 == 0:
        string = str(stone)
        halfway = len(string) // 2
        left = string[:halfway]
        right = string[halfway:]
        return transform_count(int(left), n - 1) + transform_count(int(right), n - 1)
    else:
        return transform_count(stone * 2024, n - 1)


def blink(stones, times):
    return sum([
        transform_count(s, times) for s in stones
    ])


stones = parse()
print(blink(stones, 6))
print(blink(stones, 25))
print(blink(stones, 75))
