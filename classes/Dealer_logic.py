"""
Dealer logic program
Follows simple logic asking for more cards until its hand gets to 16 or above 
also has a method to show its first card as a string 

Returns:
    _type_: _description_
"""

from .Deck import Deck
from .Hand_logic import Hand


class Dealer:
    def __init__(self):
        self._hand = Hand_logic.Hand  # Dealer’s hand, assuming a Hand class is defined
        
    @property
    def hand(self):
        """Getter for the dealer's hand."""
        return self._hand

    def receive_card(self, card):
        """Add a card to the dealer's hand."""
        self._hand.hit(card)

    def play_turn(self):
        """
        The dealer's logic for playing their turn:
        - Draws cards until reaching at least a value of 16.
        - Stops drawing if the hand value is 16 or more.
        - Finally return the value of their hand
        """
        while self._hand.GetScore < 16:
            self._hand.hit()
    def DealerScore(self) -> int:
        """
        Methond to get the dealers score

        Returns:
            int: Value of hand
        """
        return self._hand.GetScore
    
    def show_first_card(self) -> Hand_logic.Card_logic.Card:
        """
        Show only the dealer's first card (to partially reveal the hand at the beginning of the game).
        Useful for games where the dealer's full hand is hidden initially.
        """
        return self._hand.

    def __repr__(self):
        return f"Dealer's hand: {self._hand}"
