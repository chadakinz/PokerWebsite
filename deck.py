from phevaluator import Card
import random
import numpy as np
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

class Deck:
    def __init__(self):
        self.cards = list()
        suits = ['c', 'd', 'h', 's']
        for suit in suits:
            for i in range(2, 15):
                self.cards.append(Card(suit, i))

    def remove_card(self, card):
        self.cards.remove(card)
        pass
    def deal_cards(self, num):
        cards = []
        np.random.shuffle(self.cards)
        for i in range(num):
            x = random.choice(self.cards)
            cards.append[x]
            self.remove_card(x)
        return cards
    def choose_cards(self):