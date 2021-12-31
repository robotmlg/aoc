
class School:

    def __init__(self, data: str):
        ints = [int(n) for n in data.split(',')]
        self.fish = [ints.count(i) for i in range(0, 9)]

    def step(self, steps: int = 1) -> int:
        for i in range(0, steps):
            new_fish = self.fish.pop(0)
            self.fish[6] += new_fish
            self.fish.append(new_fish)
        return sum(self.fish)


def day6(steps: int):
    with open("day6.txt") as f:
        school = School(f.readline())
    return school.step(steps)


if __name__ == "__main__":
    print(day6(80))
    print(day6(256))
