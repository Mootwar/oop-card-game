from .Deck_logic import Deck
from .player_logic import Player
from .Dealer_logic import Dealer


class Game:
    def __init__(self):
        numOfCards = self.GUI()
        self.GameDeck = Deck(numOfCards)
        self.Player = Player(self.GameDeck)
        self.Dealer = Dealer(self.GameDeck)

    def start_game(self):
        self.PlayGame()

    def GUI(self):
        """
        Display the graphical user interface for the game.

        Returns:
            str: Number of decks selected by the user.
        """
        print("Welcome to Black Jack!")
        print("""Select how many standard decks
do you want in the game to begin the game!""")
        num = input()
        return num

    def PlayGame(self):
        """
        Main logic of the game where the player's
        and dealer's turns are played,
        and the results are displayed.
        """
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
                print("It's a tie!")
            else:
                print("You win!")
        else:
            if self.Player._hand.is_bust():
                print("You lose!")
            else:
                if int(player_score) > dealer_score:
                    print("You win!")
                elif int(player_score) < dealer_score:
                    print("You lose!")
                else:
                    print("It's a tie!")
