# oop-card-game
textualize.io


"""Player class
    Handles the cards a player currently holds
"""
import Deck
import Hand_logic

class Player:
    def __init__ (self):
        self._hand = Hand_logic.hand()
    
    def receive_card(self,card):
        self._hand.add_card(card)
        
    def play_turn(self,deck):
        """
        The player's logic for playing their turn:
        - User can hit or user can stay.
        """
        isPlayerTurn = True
        while (isPlayerTurn):
            print("current value: ",self._hand.value)
            playerChoice = input("h to hit, s to stay: ")
            if playerChoice == "H" or "h":
                self._hand.add_card(deck.draw_card())
                if self._hand.isBust():
                    print (self._hand.value," is bust :(")
                    isPlayerTurn = False
            elif playerChoice == "S" or "s":
                isPlayerTurn = False
            else:
                raise Exception("invalud input")
    
    def __repr__(self):
        return f"Player's hand: {self._hand}"
