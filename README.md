# oop-card-game
textualize.io

"""Player class Handles the cards a player currently holds """ 
from classes.Deck_logic import Deck
from classes.Hand_logic import Hand

class Player: 
    def __init__ (self, _deck): 
        self.game_deck = _deck
        self._hand = Hand(self.game_deck)

    def receive_card(self,card):
        self._hand.add_card(card)

    def printHand(self):
        print("Current Hand:")
        for card in self._hand.cards:
            print(card.__repr__())
        
    def play_turn(self):
        """
        The player's logic for playing their turn:
        - User can hit or user can stay.
        """
        isPlayerTurn = True
        self._hand.hit()
        self._hand.hit()
        while (isPlayerTurn):
            self.printHand()
            print("current value: ",self._hand.GetScore())
            playerChoice = input("h to hit, s to stay: ")
            if (playerChoice == "h" or playerChoice == "H"):
                self._hand.hit()
                if self._hand.is_bust():
                    print (self._hand.GetScore()," is bust :(")
                    isPlayerTurn = False
            elif (playerChoice == "s"):
                isPlayerTurn = False
                break
            else:
                raise Exception("invalud input")
        print("Turn ended!")

    def __repr__(self):
        return f"Player's hand: {self._hand}"
