from typing import List
from .Card import Card
import random

class DeckCards:

  def __init__(self, cards:List[Card]) -> None:
    self._player_turn: int = 0
    # init cards on deck
    self._opposite_cards:List[Card] = cards
    card = self._remove_random_element(self._opposite_cards, (0, 35))
    self._board_cards = [card]
  
  def draw_n_cards(self, n) -> List[Card]:
    return [self.draw_card() for _ in range(n)]
  
  def draw_card(self) -> Card:
    #Check if there is remain cards
    if self._opposite_cards:
      self._opposite_cards, self._board_cards = self._board_cards[1:], [self._opposite_cards[0]]
    #Remove a random card
    return self._remove_random_element(self._opposite_cards)  
  

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

    return random_element



  # Getter for _player_turn
  @property
  def player_turn(self) -> int:
      return self._player_turn

  # Setter for _player_turn
  @player_turn.setter
  def player_turn(self, value: int) -> None:
      self._player_turn = value

  # Getter for _opposite_cards
  @property
  def opposite_cards(self) -> List[Card]:
      return self._opposite_cards

  # Setter for _opposite_cards
  @opposite_cards.setter
  def opposite_cards(self, cards: List[Card]) -> None:
      self._opposite_cards = cards

  # Getter for _board_cards
  @property
  def board_cards(self) -> List[Card]:
      return self._board_cards

  # Setter for _board_cards
  @board_cards.setter
  def board_cards(self, cards: List[Card]) -> None:
      self._board_cards = cards

  
  def __str__(self) -> str:
        opposite_cards_str = ', '.join(map(str, self._opposide_cards))
        board_cards_str = ', '.join(map(str, self._board_cards))
        return f"Player Turn: {self._player_turn}\nOpposite Cards: {opposite_cards_str}\nBoard Cards: {board_cards_str}"
