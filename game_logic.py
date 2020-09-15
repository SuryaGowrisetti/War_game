import deck
import player

a_deck = deck.Deck()
a_deck.shuffle() # shuffling the deck

player1 = player.Player('Surya')
player2 = player.Player('Chandu')

for i in range(int(len(a_deck.cards)/2)):
    player1.cards.append(a_deck.deal_one())
    player2.cards.append(a_deck.deal_one())

game_on = True

round_num = 0
while game_on == True:
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
            player1.add_cards(player_two_cards)
            player1.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player2.add_cards(player_two_cards)
            player2.add_cards(player_one_cards)
            at_war = False
        elif player_two_cards[-1].value == player_two_cards[-1].value:
            print('WARR')
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

