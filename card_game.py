from random import shuffle
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# for each in new_deck.cards:
#     print(each.rank,each.suit,each.value)

class Deck():
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        return [each.__str__() for each in self.cards]

    def shuffle(self):
        shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return f'{self.name} has {len(self.cards)} cards'

    def remove_one(self):
        return self.cards.pop(0)

    def add_cards(self, new_cards):
        # for multiple card objects
        if type(new_cards) is list:
            self.cards.extend(new_cards)
        # for a single card object
        else:
            self.cards.append(new_cards)


a_deck = Deck()
a_deck.shuffle()  # shuffling the deck

player1 = Player('Surya')
player2 = Player('Chandu')

for i in range(int(len(a_deck.cards)/2)):
    player1.cards.append(a_deck.deal_one())
    player2.cards.append(a_deck.deal_one())

game_on = True

round_num = 0
while game_on is True:
    round_num += 1
    print(f"Round {round_num}")

    if len(player1.cards) == 0:
        print(f"{player1.name} has lost")
        game_on = False
        break
    elif len(player2.cards) == 0:
        print(f"{player2.name} has lost")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player1.remove_one())
    player_two_cards = []
    player_two_cards.append(player2.remove_one())

    at_war = True

    while at_war == True:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player1.add_cards(player_one_cards)
            player1.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player2.add_cards(player_one_cards)
            player2.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR!!")
            if len(player1.cards) < 10:
                print(f'{player1.name} has no cards left and loses')
                print(f'{player2.name} has won the game')
                game_on = False
                break
            elif len(player2.cards) < 10:
                print(f'{player2.name} has no cards left and loses')
                print(f'{player1.name} has won the game')
                game_on = False
                break
            else:
                for num in range(10):
                    player_one_cards.append(player1.remove_one())
                    player_two_cards.append(player2.remove_one())
