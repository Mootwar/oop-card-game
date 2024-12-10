"""
Dealer logic program
Follows simple logic asking for more cards until its hand gets to 16 or above
also has a method to show its first card as a string

Returns:
    _type_: _description_
"""

from .Hand_logic import Hand


class Dealer:
    def __init__(self, _deck):
        self._hand = Hand(_deck)
        self._hand.hit()
        self._hand.hit()

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
        - Finally return the value of their hand.
        """
        while self._hand.GetScore() < 16:
            self._hand.hit()
        return self._hand.GetScore()  # Return the dealer's final score

    def DealerScore(self) -> int:
        """
        Methond to get the dealers score

        Returns:
            int: Value of hand
        """
        return self._hand.GetScore()

    def show_first_card(self):
        """
        Show only the dealer's first card
        (to partially reveal the hand at the beginning of the game).
        Useful for games where the dealer's full hand is hidden initially.
        """
        if self._hand.cards:
            return self._hand.cards[0]

        return None

    def printHand(self):
        print("Dealer's Hand:")
        for card in self._hand.cards:
            print(card.__repr__())
