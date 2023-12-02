
def parse_games():
    games = {}
    with open("in.txt", "r") as f:
        for l in f:
            prefix, game_str = l.split(": ")
            game_num = int(prefix.split(" ")[1])

            rounds = game_str.strip().split("; ")
            game = []
            for r in rounds:
                pulls = r.split(", ")
                round = {}
                for p in pulls:
                    n, color = p.split(" ")
                    round[color] = int(n)
                game.append(round)

            games[game_num] = game

    return games


def part1(games):
    sum = 0
    for n, game in games.items():
        valid = True
        for r in game:
            if r.get("red", 0) > 12 or r.get("green", 0) > 13 or r.get("blue", 0) > 14:
                valid = False
                break

        if valid:
            sum += n
        
    print(sum)


def part2(games):
    sum = 0
    for n, game in games.items():
        mins = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for r in game:
            mins["red"] = max(mins["red"], r.get("red", 0))
            mins["green"] = max(mins["green"], r.get("green", 0))
            mins["blue"] = max(mins["blue"], r.get("blue", 0))

        sum += (mins["red"] * mins["green"] * mins["blue"])

        
    print(sum)


games = parse_games()
part1(games)
part2(games)
