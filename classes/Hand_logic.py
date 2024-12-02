"""Hand class
    Handles the cards a player currently holds
"""
from .Card_logic import Card
from .Deck_logic import Deck

class Hand:
    def __init__(self, deck: Deck):
        self.cards: list[Card] = []
        self.score = 0
        self.deck = deck

    def hit(self):
        # Add a card to the hand and update the score.
        self.cards.append(self.deck.GiveCard())
        self.update_score()
   
    def GetScore(self)-> int:
        return (self.score)
    
    def update_score(self):
        # Calculate the total score for the hand.
        self.score = sum(card.value[0] for card in self.cards)
        ace_count = sum(1 for card in self.cards if card.rank == 11)
        while self.score > 21 and ace_count > 0:
            self.score -= 10
            ace_count -= 1

    def is_bust(self):
        # Return True if the hand's score exceeds 21.
        return self.score > 21

    def is_black_jack(self):
        return self.score == 21
