from Hand_logic import Hand
import Deck

class Player:
    def __init__(self, hand):
        self.hand = Hand(hand)

    def printHand(self):
        for card in self.hand:
            print(card.__repr__())
    def process(self):
        self.hand.hit()
        if self.hand.is_bust():
            print("bussssss")
            return
        self.hand.hit()
    def printInfo(self):
        for card in self.hand.cards:
            card.__repr__()
        print("Total value is: " + self.hand.score)

class Game:
    def __init__(self):
        numOfCards = self.GUI()
        self.GameDeck = Deck(numOfCards)
        self.Player = Player(self.GameDeck)


    def GUI(self):
        print("Welcome to Black Jack!")
        print("Select how many standard decks do you want in the game to begin the game!")
        num = input()
        return num

    def PlayGame(self):
        self.Player.process()


        