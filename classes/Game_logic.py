from .Hand_logic import Hand
from .Deck_logic import Deck
from .player_logic import Player
from .Dealer_logic import Dealer

class Game:
    def __init__(self):
        numOfCards = self.GUI()
        self.GameDeck = Deck(numOfCards)
        self.Player = Player(self.GameDeck)
        self.Dealer = Dealer(self.GameDeck)
        self.PlayGame()


    def GUI(self):
        print("Welcome to Black Jack!")
        print("Select how many standard decks do you want in the game to begin the game!")
        num = input()
        return num

    def PlayGame(self):
        print(str(self.Dealer.show_first_card()))
        self.Player.play_turn()
        self.Dealer.play_turn()
        dealer_score = self.Dealer.DealerScore()
        player_score = self.Player._hand.GetScore()
        self.Dealer.printHand()
        print("Dealer's score: " + str(dealer_score))
        print("Your score: " + str(player_score))

        if self.Dealer._hand.is_bust():
            if self.Player._hand.is_bust():
                print("its a tie!")
            else:
                print("you win!")
        else:
            if self.Player._hand.is_bust():
                print("you lose!")
            else:
                if int(player_score) > dealer_score:
                    print("you win!")
                elif int(player_score) < dealer_score:
                    print("you lose!")
                else:
                    print("its a tie!")


