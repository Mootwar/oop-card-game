"""Hand class
    Handles the cards a player currently holds
"""
import Card

class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0

    def hit(self, card: Card):
        # Add a card to the hand and update the score.
        self.cards.append(card)
        self.update_score()

    def update_score(self):
        # Calculate the total score for the hand.
        self.score = sum(card.value for card in self.cards)
        ace_count = sum(1 for card in self.cards if card.rank == 11)
        while self.score > 21 and ace_count > 0:
            self.score -= 10
            ace_count -= 1

    def is_bust(self):
        # Return True if the hand's score exceeds 21.
        return self.score > 21
