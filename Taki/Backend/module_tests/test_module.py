import unittest
import sys
sys.path.append("/Users/ywblhytr/Desktop/Games/Taki/Backend")

from Buissines.Card import Card
from Buissines.DeckCards import DeckCards
from Buissines.Game import Game
from tests import Tests


cards = ['1-yelllow', '1-blue', '1-red', '1-green', 
    '2-yelllow', '2-blue' , '2-red', '2-green', 
    '3-yelllow', '3-blue', '3-red', '3-green',
    '4-yelllow', '4-blue', '4-red', '4-green',
    '5-yelllow', '5-blue', '5-red', '5-green',
    '6-yelllow', '6-blue', '6-red', '6-green',
    '7-yelllow', '7-blue', '7-red', '7-green',
    '8-yelllow', '8-blue', '8-red', '8-green',
    '9-yelllow', '9-blue', '9-red', '9-green',
    'ChangeDirection-yelllow', 'ChangeDirection-blue', 'ChangeDirection-red', 'ChangeDirection-green', 
    'Plus-yelllow', 'Plus-blue', 'Plus-red', 'Plus-green', 
    'Stop-yelllow', 'Stop-blue', 'S-red', 'S-green', 
    '+2-yelllow', '+2-blue', '+2-red', '+2-green', 
    'Taki-yelllow', 'Taki-blue', 'Taki-red', 'Taki-green', 'Taki-colorfull', 
    'ChangeColor' 
    ]

class DeckCardsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cards_obj = [Card(c) for c in cards]
        return super().setUp()
    
    def test_initial_deck(self):
        init_cards = self.cards_obj[0:35]
        deck_cards = DeckCards(self.cards_obj.copy())
        board_cards = deck_cards.board_cards
        self.assertEqual(len(board_cards), 1)
        self.assertIn(board_cards[0], init_cards)
        self.assertNotIn(board_cards[0], deck_cards.opposite_cards)

        self.cards_obj.remove(board_cards[0])
        self.assertEqual(self.cards_obj, deck_cards.opposite_cards)
        
class GameTest(unittest.TestCase):
    def test_create_game(self):
        cards_obj = [Card(c) for c in cards]


if __name__ == '__main__':
    unittest.main()



