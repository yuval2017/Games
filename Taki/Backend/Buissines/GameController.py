
from typing import List, Dict
from Game import *
from DeckCards import *
from Card import *

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
class GameController:
  def __init__(self) -> None:
    self.next_id = 0
    self._games: Dict[id, Game] = dict()
     
  def ceate_new_game(self)->List[Card]:
    cards = [Card(c) for c in cards]
    self._games[self.next_id] = DeckCards(cards)
    return cards

  def add_cards_to_board(self, game_id, cards: List[Card], visitor:Visitor) -> Exception | None:
    if game_id not in self._games:
      raise Exception("No game with id: " + game_id)
    self._games[game_id].add_cards_on_board(cards)
  
  def draw_card(self, game_id, visitor) -> Card | Exception:
    if game_id not in self._games:
      raise Exception("No game with id: " + game_id)
    return self._games[game_id].draw_card(visitor)
  