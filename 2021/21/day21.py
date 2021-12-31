

def parse_input(filename):
    positions = []
    with open(filename) as f:
        for line in f:
            positions.append(int(line.strip().split(" ")[-1]))
    # subtract one from each starting position so they're 0 indexed
    return list(map(lambda x: x - 1, positions))


class Game:

    class Die:

        def __init__(self):
            self.value = 0
            self.rolls = 0

        def next(self, rolls=1):
            if rolls == 1:
                self.value = self.value + 1 if self.value < 100 else 1
                self.rolls += 1
                return self.value
            return sum([self.next() for _ in range(rolls)])

    def __init__(self, starting_positions):
        self.positions = starting_positions
        self.scores = [0] * len(self.positions)
        self.die = self.Die()

    def play(self):
        curr_player = 0
        while max(self.scores) < 1000:
            roll = self.die.next(3)
            self.positions[curr_player] = (self.positions[curr_player] + roll) % 10
            self.scores[curr_player] += self.positions[curr_player] + 1
            curr_player = (curr_player + 1) % len(self.positions)

        return min(self.scores) * self.die.rolls


cache = {}


def dirac(win_score, positions, scores=None, curr_player=0):
    if scores is None:
        scores = [0] * len(positions)

    wins = [0] * len(positions)
    if max(scores) >= win_score:
        wins[scores.index(max(scores))] = 1
        return wins

    key = (tuple(positions), tuple(scores))
    if key in cache:
        return cache[key]

    new_player = (curr_player + 1) % len(positions)
    for roll1 in [1, 2, 3]:
        for roll2 in [1, 2, 3]:
            for roll3 in [1, 2, 3]:
                roll = roll1 + roll2 + roll3
                new_positions = list(positions)
                new_positions[curr_player] = (positions[curr_player] + roll) % 10

                new_scores = list(scores)
                new_scores[curr_player] += new_positions[curr_player] + 1

                new_wins = dirac(win_score, new_positions, new_scores, new_player)

                wins = [wins[i] + new_wins[i] for i in range(len(wins))]

    cache[key] = wins
    return wins


if __name__ == "__main__":
    file = "day21ex.txt"
    print(Game(parse_input(file)).play())
    print(dirac(21, parse_input(file)))
