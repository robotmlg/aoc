import sys


def day7(fuel_eq):
    with open("day7.txt") as f:
        crabs = [int(i) for i in f.readline().split(",")]
        min_fuel = sys.maxsize

        for i in range(max(crabs)):
            fuel = sum([abs(fuel_eq(c, i)) for c in crabs])
            if fuel < min_fuel:
                min_fuel = fuel
        return min_fuel


def quicksum(n):
    # shortcut for sum_1^n n
    return (n * (n + 1)) // 2


if __name__ == "__main__":
    print(day7(lambda c, i: abs(c - i)))
    print(day7(lambda c, i: quicksum(abs(c - i))))