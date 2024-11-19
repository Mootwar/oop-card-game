"""Card class
    Handles the card states and uses encapsulation with property tags to secure data 
    security and immutability
Returns:
    _type_: _description_
"""
from enum import Enum

class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11  # Handle flexible value in game logic

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self._suit = suit  # Private attribute
        self._rank = rank  # Private attribute

    @property
    def suit(self) -> Suit:
        """Getter for suit"""
        return self._suit

    @property
    def rank(self) -> Rank:
        """Getter for rank"""
        return self._rank

    def __repr__(self) -> str:
        return f"{self.rank.name.title()} of {self.suit.value}"

    @property
    def value(self) -> int:
        """Get the numerical value of the card based on rank."""
        return self._rank.value
