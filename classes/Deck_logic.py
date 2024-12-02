'''
Deck Class
Handles the deck 
'''

from .Card_logic import SUITS
from .Card_logic import RANKS
from .Card_logic import Card
import random

class Deck:
    def __init__(self, numOfDecks=1):
        self.listOfCards = []
        self.FillOutDeck(int(numOfDecks))
        self.SuffleDeck()
    
    def FillOutDeck(self, numberOfDecks):
        while(numberOfDecks > 0):
            for suit in SUITS:
                for rank in RANKS:
                    self.listOfCards.append(Card(suit, rank))
            numberOfDecks = numberOfDecks-1

    def RemoveCard(self, list, cardToBeRemoved):
        list.remove(cardToBeRemoved)

    def PrintDeck(self):
        for card in self.listOfCards:
            print(card.__repr__())

    def PrintSizeOfDeck(self):
        print(len(self.listOfCards))

    def GiveCard(self) -> Card:
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


        



