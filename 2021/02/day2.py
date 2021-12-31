
def day2A():
    horiz = 0
    depth = 0
    with open("day2.txt") as f:
        for line in f:
            instr, dist_str = line.split(' ')
            dist = int(dist_str)

            if instr == 'forward':
                horiz += dist
            elif instr == 'up':
                depth -= dist
            elif instr == 'down':
                depth += dist
            else:
                print("ERROR")

    return horiz * depth


def day2B():
    horiz = 0
    depth = 0
    aim = 0
    with open("day2.txt") as f:
        for line in f:
            instr, dist_str = line.split(' ')
            dist = int(dist_str)

            if instr == 'forward':
                horiz += dist
                depth += aim * dist
            elif instr == 'up':
                aim -= dist
            elif instr == 'down':
                aim += dist
            else:
                print("ERROR")

    return horiz * depth


# OOO solution
class Submarine:
    horiz = 0
    depth = 0
    aim = 0

    def move(self, direction, distance):
        # don't have 3.10, so no match
        if direction == 'forward':
            self.horiz += distance
            self.depth += self.aim * distance
        elif direction == 'up':
            self.aim -= distance
        elif direction == 'down':
            self.aim += distance
        else:
            print("ERROR")

    def get_answer(self):
        return self.horiz * self.depth


if __name__ == '__main__':
    sub = Submarine()
    with open("day2.txt") as f:
        for line in f:
            instr, dist_str = line.split(' ')
            dist = int(dist_str)
            sub.move(instr, dist)

    print(sub.get_answer())
