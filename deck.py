from random import *

class Card:

    def __init__(self, suit, rank):  # constructor
        self.suit = suit
        self.rank = rank


    def getSuit(self):
        return self.suit


    def getRank(self):
        return self.rank


    def blackJackValue(self):  # specific to blackjack
        if self.rank in ['J','Q','K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)


    def __str__(self):
        sustring = ''
        if self.suit == 'D':
            sustring = chr(9826)
        elif self.suit == 'S':
            sustring = chr(9824)
        elif self.suit == 'C':
            sustring = chr(9827)
        else:
            sustring = chr(9825)
        return '['+ self.rank + sustring + ']'


class Deck:
    def __init__(self):
        self.deck = []
        suits = ['H','S','C','D']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                 '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def getDeck(self):
        return self.deck

    def cardsleft(self):
        return len(self.deck)

    def dealCard(self):
        return self.deck.pop()

    def shuffleDeck(self):
        shuffle(self.deck)
        

def main():
    deck = Deck()
    deck.shuffleDeck()

    print('There are', deck.cardsleft(), 'left')
    players_hand = []

    # deal a card to the player
    players_hand.append(deck.dealCard())
    players_hand.append(deck.dealCard())
    
    print('The player was dealt: ', players_hand[0], 'and', players_hand[1])
    print('There are', deck.cardsleft(), 'left')

    '''for card in deck.getDeck():
        print(card)
    '''

if name == '__main__':
    main()
