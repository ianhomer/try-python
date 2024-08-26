from .card import Card


class Cards:
    def __init__(self, filename):
        file = open(filename, "r")
        self.cards = []
        for line in file.readlines():
            self.cards.append(Card(line))

    def count(self):
        return len(self.cards)

    def total(self):
        return sum([card.score() for card in self.cards])
