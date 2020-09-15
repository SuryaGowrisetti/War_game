import cards


class Player:
    def __init__(self,name):
        self.name = name
        self.cards = []

    def __str__(self):
        return f'{self.name} has {len(self.cards)} cards'

    def remove_one(self):
        return self.cards.pop(0)

    def add_cards(self,new_cards):
        # for multiple card objects
        if type(new_cards) is list:
            self.cards.extend(new_cards)
        # for a single card object
        else:
            self.cards.append(new_cards)

# player_surya = Player('Surya') 
# my_card = cards.Card('Spades','Ace')
# player_surya.add_cards(my_card)
