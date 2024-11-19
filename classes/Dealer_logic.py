"""
Dealer logic program
Follows simple logic asking for more cards until its hand gets to 16 or above 
also has a method to show its first card as a string 

Returns:
    _type_: _description_
"""
import Deck

class Dealer:
    def __init__(self):
        self._hand = Hand()  # Dealer’s hand, assuming a Hand class is defined

    @property
    def hand(self):
        """Getter for the dealer's hand."""
        return self._hand

    def receive_card(self, card):
        """Add a card to the dealer's hand."""
        self._hand.add_card(card)

    def play_turn(self, deck):
        """
        The dealer's logic for playing their turn:
        - Draws cards until reaching at least a value of 16.
        - Stops drawing if the hand value is 16 or more.
        """
        while self._hand.value < 16:
            self._hand.add_card(deck.draw_card())

    def show_first_card(self):
        """
        Show only the dealer's first card (to partially reveal the hand at the beginning of the game).
        Useful for games where the dealer's full hand is hidden initially.
        """
        if self._hand.cards:
            return self._hand.cards[0]
        return None

    def __repr__(self):
        return f"Dealer's hand: {self._hand}"
