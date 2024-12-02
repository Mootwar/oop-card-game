from .Hand_logic import Hand
from .Deck_logic import Deck
from .player_logic import Player
'''
class Player:
    def __init__(self, Deck):
        self.hand = Hand(Deck)

    def printHand(self):
        print("Current Hand:")
        for card in self.hand.cards:
            print(card.__repr__())
    def process(self):
        while True:
            self.hand.hit()
            self.printHand()
            self.printInfo()
            if self.hand.is_bust():
                print("bust")
                break
    def printInfo(self):
        for card in self.hand.cards:
            card.__repr__()
        print("Total value is: " + str(self.hand.score))
'''
class Game:
    def __init__(self):
        numOfCards = self.GUI()
        self.GameDeck = Deck(numOfCards)
        self.Player = Player(self.GameDeck)
        self.PlayGame()


    def GUI(self):
        print("Welcome to Black Jack!")
        print("Select how many standard decks do you want in the game to begin the game!")
        num = input()
        return num

    def PlayGame(self):
        self.Player.play_turn()

