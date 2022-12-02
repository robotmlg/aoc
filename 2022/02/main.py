
class Round():

    def __init__(self, string: str):
        parts = string.split()

        self.opponent = parts[0]
        self.me = parts[1]
        self.goal = parts[1]


    @staticmethod
    def get_score(opp, me):
        score = 0
        match me:
            case "X":
                score += 1
            case "Y":
                score += 2
            case "Z":
                score += 3
            case _:
                raise Exception

        # tie
        if ord(me) - ord("X") == ord (opp) - ord("A"):
            score += 3
        # loss
        elif (opp == "A" and me == "Z") or (opp == "B" and me == "X") or (opp == "C" and me == "Y"):
            score += 0
        # win
        else:
            score += 6

        return score


    def get_score_pt_1(self):
        return self.get_score(self.opponent, self.me)


    def get_score_pt_2(self):
        opp_num = ord(self.opponent) - ord("A")
        match self.goal:
            case "X":  # lose
                delta = (opp_num - 1) % 3
                me = chr(ord("X") + delta)
            case "Y":  # draw
                me = chr(ord("X") + opp_num)
            case "Z":  # win
                delta = (opp_num + 1) % 3
                me = chr(ord("X") + delta)
            case _:
                raise Exception

        return self.get_score(self.opponent, me)


def main():

    rounds = []
    with open("in.txt") as f:
        for line in f:
            rounds.append(Round(line))

    print(sum([r.get_score_pt_1() for r in rounds]))
    print(sum([r.get_score_pt_2() for r in rounds]))

main()
