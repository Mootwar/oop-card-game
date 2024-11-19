"""Card class
    Handles the card states and uses encapsulation with property tags to secure data 
    security and immutability.
    
Returns:
    Card: A playing card with a suit and rank, along with its associated value.
"""

from typing import Dict, Tuple

# Define dictionaries for suits and ranks
SUITS = {
    "hearts": "Hearts",
    "diamonds": "Diamonds",
    "clubs": "Clubs",
    "spades": "Spades"
}

RANKS = {
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack": 10,
    "queen": 10,
    "king": 10,
    "ace": 11  # Handle flexible Ace value in Hand or Dealer logic
}

class Card:
    def __init__(self, suit: str, rank: str):
        # Check that suit and rank are valid
        if suit.lower() not in SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank.lower() not in RANKS:
            raise ValueError(f"Invalid rank: {rank}")

        # Set private attributes
        self._suit = SUITS[suit.lower()]
        self._rank = rank.lower()

    @property
    def suit(self) -> str:
        """Getter for suit"""
        return self._suit

    @property
    def rank(self) -> str:
        """Getter for rank"""
        return self._rank

    def __repr__(self) -> str:
        return f"{self.rank.title()} of {self.suit}"

    @property
    def value(self) -> Tuple[int, str]:
        """Get a tuple of the numerical value of the card and the suit."""
        return RANKS[self._rank], self._suit
