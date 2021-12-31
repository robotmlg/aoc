from toolz import partition


class Bingo:

    def __init__(self, board_str: tuple):
        self.board = []
        self.marks = []
        self.called = []

        for row in board_str:
            self.board.append([int(n) for n in row.split()])
            self.marks.append([False] * len(self.board[-1]))

        self.size = len(self.board)

    def call(self, num) -> bool:
        self.called.append(num)

        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.board[i][j] == num:
                    self.marks[i][j] = True
                    return True
        return False

    def check_win(self) -> bool:
        # rows
        for i in range(0, self.size):
            if all(self.marks[i]):
                return True
        # columns
        for j in range(0, self.size):
            column = [self.marks[i][j] for i in range(0, self.size)]
            if all(column):
                return True
        return False

    def score(self) -> int:
        unmarked_sum = 0
        for i in range(0, self.size):
            for j in range(0, self.size):
                if not self.marks[i][j]:
                    unmarked_sum += self.board[i][j]
        return unmarked_sum * self.called[-1]


def parse_input():
    with open("day4.txt") as f:
        numbers_str = f.readline()
        numbers = [int(n) for n in numbers_str.split(',')]

        # skip blank line
        f.readline()

        all_boards = [line.strip() for line in f.readlines() if line != "\n"]
        boards = list(partition(5, all_boards))

        return numbers, boards


def day4A():
    numbers, board_strs = parse_input()

    bingos = [Bingo(s) for s in board_strs]

    for n in numbers:
        for b in bingos:
            b.call(n)
            if b.check_win():
                return b.score()


def day4B():
    numbers, board_strs = parse_input()

    bingos = [Bingo(s) for s in board_strs]

    for n in numbers:
        for b in bingos:
            b.call(n)
        if len(bingos) == 1 and bingos[0].check_win():
            return bingos[0].score()
        bingos = [b for b in bingos if not b.check_win()]


if __name__ == "__main__":
    print(day4A())
    print(day4B())