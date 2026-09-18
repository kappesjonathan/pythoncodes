#Quiero buscar formas para interactucar y mezclar listas.
#Un ejemplo de esto puede ser representar un mazo de cartas...

#En un mazo de cartas tenemos 52 cartas.
#13 cartas de cada palo (4)

cards_suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
cards_number = ["A", "1", "2", "3" , "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck_of_cards = []

import random

#FORMA 1
for number in cards_number:
    for suit in cards_suits:
        card = (number, suit)
        deck_of_cards.append(card)
print(deck_of_cards)

# #FORMA 2
# deck_of_cards = [
#     (number, suit)
#     for suit in cards_suits
#     for number in cards_number
# ]
# print(deck_of_cards)

# #FORMA 3
# from itertools import product
# deck_of_cards = list(product(cards_number, cards_suits))
# print(deck_of_cards)

input()
def shuffle_deck():
    shuffled_deck = random.shuffle(deck_of_cards)
    print(shuffled_deck)


    

