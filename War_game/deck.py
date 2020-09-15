import random
import cards


class Deck():
    def __init__(self):
        self.cards = []
        for suit in cards.suits:
            for rank in cards.ranks:
                self.cards.append(cards.Card(suit, rank))

    def __str__(self):
        return [each.__str__() for each in self.cards]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()