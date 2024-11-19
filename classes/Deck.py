'''
Deck Class
Handles the deck 
'''

import Card
import random

class Deck:
    def __init__(self, numOfDecks=1):
        self.listOfCards = []
        self.FillOutDeck(numOfDecks)
    
    def FillOutDeck(self, numberOfDecks):
        while(numberOfDecks > 0):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    self.listOfCards.append(Card.Card(suit, rank))
            numberOfDecks = numberOfDecks-1

    def RemoveCard(self, list, cardToBeRemoved):
        list.remove(cardToBeRemoved)

    def PrintDeck(self):
        for card in self.listOfCards:
            print(card.__repr__())

    def PrintSizeOfDeck(self):
        print(len(self.listOfCards))

    def GiveCard(self):
        cardToGive = self.listOfCards[random.randint(0, len(self.listOfCards)-1)]
        self.RemoveCard(self.listOfCards,cardToGive)
        return cardToGive
    
    def SuffleDeck(self):
        newDeck = []
        oldDeck = self.listOfCards
        while(len(oldDeck) > 0):
            curCard = oldDeck[random.randint(0, len(oldDeck) -1)]
            self.RemoveCard(self.listOfCards,curCard)
            newDeck.append(curCard)
        self.listOfCards = newDeck


        



