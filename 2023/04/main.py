import re

class Card:
    
    def __init__(self, line: str):
        parts = re.match(r"Card\s+(\d+):\s+([0-9 ]+) \|\s+([0-9 ]+)", line.strip())
        self.id = int(parts.group(1))
        self.winners = [int(n) for n in parts.group(2).split(" ") if len(n) > 0]
        self.numbers = [int(n) for n in parts.group(3).split(" ") if len(n) > 0]

    def points(self):
        matches = self.win_count()
        return 2**(matches-1) if matches >= 1 else 0

    def win_count(self):
        return sum([1 for n in self.winners if n in self.numbers])


def parse_input():
    cards = {}
    with open("in.txt", "r") as f:
        for l in f:
            card = Card(l)
            cards[card.id] = card
    return cards


def part2(cards):
    wins_per_card = {i: None for i in range(1, len(cards) + 1)}

    used_cards = 0
    for i in range(len(cards), 0, -1):
        curr = cards[i]
        
        win_count = curr.win_count()
        used_cards += 1
        if win_count == 0:
            wins_per_card[i] = 0
            continue

        won_cards = win_count
        new_cards = [curr.id + j for j in range(1, win_count + 1)]
        while len(new_cards) > 0:
            nc = new_cards.pop(0)
            won_cards += wins_per_card[nc]
        used_cards += won_cards
        wins_per_card[i] = won_cards

    return used_cards
        

cards = parse_input()
# part1
print(sum([c.points() for c in cards.values()]))
print(part2(cards))

