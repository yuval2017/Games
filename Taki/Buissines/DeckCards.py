from typing import List
from Card import *
import random

class DeckCards:

  def __init__(self, cards:List[Card]) -> None:
    
    self._player_turn: int = 0

    # init cards on deck
    self._opposide_cards:List[Card] = cards
    card = self._remove_random_element(self._opposide_cards, (0, 35))
    self._board_cards = [card]
        
  def draw_n_cards(self, n) -> List[Card]:
    return [self.draw_card() for _ in range(n)]
  
  def draw_card(self) -> Card:
    #Check if there is remain cards
    if self._opposide_cards:
      self._opposide_cards, self._board_cards = self._board_cards[1:], [self._opposide_cards[0]]
    #Remove a random card
    return self._remove_random_element(self._opposide_cards)  
  

  def append_cards(self, cards:List[Card]):
    self._board_cards.append(cards)

  def _remove_random_element(self, arr, interval = None):
    if interval is None:
      interval = (0, len(arr))
    if not arr:
        return None  # Return None if the array is empty
    
    if interval is None:
      interval = (0, len(arr) - 1)

    # Step 1: Generate a random index
    random_index = random.randint(*interval)

    # Step 2: Get the element at the random index
    random_element = arr[random_index]

    # Step 3: Remove the element from the array
    del arr[random_index]


