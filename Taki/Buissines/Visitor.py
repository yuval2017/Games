from Card import *
from typing import List
class Visitor:
  def __init__(self, id, game_position: int, cards: List[Card] = None) -> None:
    self._id = id
    self._game_position: int = game_position
    self._cards = cards
  @property
  def cards(self) -> List[Card]:
    return self._cards
  def give_cards(self, cards) -> None:
    self._cards = cards

  def finished_cards(self) -> bool:
    return len(self._cards) == 0
  