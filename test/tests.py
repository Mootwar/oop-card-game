import unittest
import io
from unittest.mock import patch, MagicMock
from classes import Card_logic
from classes import player_logic
from classes import Dealer_logic
from classes import Deck_logic
from classes import Game_logic
from classes import Hand_logic

class TestCardLogic(unittest.TestCase):
    def test_card_creation(self):
      card = Card_logic.Card("hearts", "ace")
      self.assertEqual(card.suit, "Hearts")
      self.assertEqual(card.rank, "ace")
      self.assertEqual(card.value, (11, "Hearts"))
      self.assertEqual(card.__repr__(), "Ace of Hearts")
      

    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            Card_logic.Card("invalid_suit", "ace")

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            Card_logic.Card("hearts", "invalid_rank")

class TestDealerLogic(unittest.TestCase):
    def test_dealer_initialization(self):
        deck = Deck_logic.Deck(1)
        dealer = Dealer_logic.Dealer(deck)
        self.assertEqual(len(dealer._hand.cards), 2)

    def test_dealer_play(self):
        deck = Deck_logic.Deck(1)
        dealer = Dealer_logic.Dealer(deck)
        dealer.play_turn()
        self.assertGreaterEqual(dealer.DealerScore(), 16)

    def test_dealer_play_final_score(self):
        deck = Deck_logic.Deck(1)
        dealer = Dealer_logic.Dealer(deck)
        final_score = dealer.play_turn()
        self.assertGreaterEqual(final_score, 16)

    def test_dealer_hand_initialization(self):
        deck = Deck_logic.Deck(1)
        dealer = Dealer_logic.Dealer(deck)
        self.assertEqual(len(dealer._hand.cards), 2)
        self.assertTrue(all(isinstance(card, Card_logic.Card) for card in dealer._hand.cards))

    def test_dealer_hand_property(self):
        deck = Deck_logic.Deck(1)
        dealer = Dealer_logic.Dealer(deck)
        hand = dealer.hand
        self.assertEqual(hand, dealer._hand)
        self.assertEqual(len(hand.cards), 2)

    def test_receive_card(self):
        deck = Deck_logic.Deck(1)
        dealer = Dealer_logic.Dealer(deck)
        initial_hand_size = len(dealer._hand.cards)
        new_card = Card_logic.Card("hearts", "ten")
        dealer.receive_card(new_card)
        self.assertEqual(len(dealer._hand.cards), initial_hand_size + 1)
        self.assertIn(new_card, dealer._hand.cards)

    def test_show_first_card(self):
        deck = Deck_logic.Deck(1)
        dealer = Dealer_logic.Dealer(deck)
        first_card = dealer.show_first_card()
        self.assertIsNotNone(first_card)
        self.assertEqual(first_card, dealer._hand.cards[0])

    def test_show_first_card_empty_hand(self):
        deck = Deck_logic.Deck(1)
        dealer = Dealer_logic.Dealer(deck)
        dealer._hand.cards = []
        first_card = dealer.show_first_card()
        self.assertIsNone(first_card)

    def test_print_hand(self):
        deck = Deck_logic.Deck(1)
        dealer = Dealer_logic.Dealer(deck)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            dealer.printHand()
            output = mock_stdout.getvalue()
        self.assertIn("Dealer's Hand:", output)
        self.assertTrue(any(card.__repr__() in output for card in dealer._hand.cards))

  
class TestGameLogic(unittest.TestCase):
    @patch('builtins.input', return_value='1')
    def test_game_initialization(self, mock_input):
        game = Game_logic.Game()
        self.assertIsInstance(game.Player, player_logic.Player)
        self.assertIsInstance(game.Dealer, Dealer_logic.Dealer)

    @patch('builtins.input', return_value='1')
    def test_GUI(self, mock_input):
        game = Game_logic.Game()
        result = game.GUI()
        self.assertEqual(result, '1')

    @patch('builtins.input', side_effect=['1', 'h', 's'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_PlayGame(self, mock_stdout, mock_input):
        game = Game_logic.Game()
        with patch.object(game.Dealer._hand, 'is_bust', side_effect=[True, False]):
            with patch.object(game.Player._hand, 'is_bust', side_effect=[True, False]):
                with patch.object(game.Player._hand, 'GetScore', return_value=18):
                    with patch.object(game.Dealer._hand, 'GetScore', return_value=16):
                        game.PlayGame()
                        output = mock_stdout.getvalue()
                        self.assertIn("You win!", output)

    @patch('builtins.input', side_effect=['1', 'h', 's'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_PlayGame_lose(self, mock_stdout, mock_input):
        game = Game_logic.Game()
        with patch.object(game.Player._hand, 'is_bust', return_value=True):
            with patch.object(game.Dealer._hand, 'GetScore', return_value=20):
                game.PlayGame()
                output = mock_stdout.getvalue()
                self.assertIn("You lose!", output)

    @patch('builtins.input', side_effect=['1', 'h', 's'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_PlayGame_dealer_wins(self, mock_stdout, mock_input):
        game = Game_logic.Game()
        with patch.object(game.Player._hand, 'is_bust', return_value=False):
            with patch.object(game.Player._hand, 'GetScore', return_value=18):
                with patch.object(game.Dealer._hand, 'GetScore', return_value=20):
                    game.PlayGame()
                    output = mock_stdout.getvalue()
                    self.assertIn("You lose!", output)

    @patch('builtins.input', side_effect=['1', 'h', 's'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_PlayGame_tie(self, mock_stdout, mock_input):
        game = Game_logic.Game()
        with patch.object(game.Dealer._hand, 'is_bust', return_value=False):
            with patch.object(game.Player._hand, 'is_bust', return_value=False):
                with patch.object(game.Player._hand, 'GetScore', return_value=18):
                    with patch.object(game.Dealer._hand, 'GetScore', return_value=18):
                        game.PlayGame()
                        output = mock_stdout.getvalue()
                        self.assertIn("It's a tie!", output)

    @patch('builtins.input', side_effect=['1', 'h', 's'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_PlayGame_you_win(self, mock_stdout, mock_input):
        game = Game_logic.Game()
        with patch.object(game.Dealer._hand, 'is_bust', return_value=False):
            with patch.object(game.Player._hand, 'is_bust', return_value=False):
                with patch.object(game.Player._hand, 'GetScore', return_value=18):
                    with patch.object(game.Dealer._hand, 'GetScore', return_value=16):
                        game.PlayGame()
                        output = mock_stdout.getvalue()
                        self.assertIn("You win!", output)

    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_game(self, mock_stdout, mock_input):
        game = Game_logic.Game()
        with patch.object(game, 'PlayGame', return_value=None) as mock_play_game:
            game.start_game()
            mock_play_game.assert_called_once()

    @patch('builtins.input', side_effect=['1', 'h', 's'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_PlayGame_both_bust(self, mock_stdout, mock_input):
        game = Game_logic.Game()
        with patch.object(game.Dealer._hand, 'is_bust', return_value=True):
            with patch.object(game.Player._hand, 'is_bust', return_value=True):
                game.PlayGame()
                output = mock_stdout.getvalue()
                self.assertIn("It's a tie!", output)

class TestPlayerLogic(unittest.TestCase):

    def test_player_repr(self):
        deck = Deck_logic.Deck(1)
        player = player_logic.Player(deck)
        representation = repr(player)
        self.assertIn("Player's hand:", representation)

    @patch('builtins.input', side_effect=['x'])
    def test_play_turn_invalid_input(self, mock_input):
        deck = Deck_logic.Deck(1)
        player = player_logic.Player(deck)
        with self.assertRaises(Exception) as context:
            player.play_turn()
        self.assertIn("invalid input", str(context.exception))

class TestHandLogic(unittest.TestCase):
    def test_update_score_with_ace_adjustment(self):
        # Create a mock deck (not used here directly)
        deck = Deck_logic.Deck(1)
        
        # Create a hand and manually add cards to ensure the condition
        hand = Hand_logic.Hand(deck)
        hand.cards = [
            Card_logic.Card("hearts", "ace"),  # Ace (value = 11)
            Card_logic.Card("spades", "king"), # King (value = 10)
            Card_logic.Card("clubs", "five")   # Five (value = 5)
        ]
        hand.update_score()
        self.assertEqual(hand.score, 16)

if __name__ == "__main__":
    unittest.main()
