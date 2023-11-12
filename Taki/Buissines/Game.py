
from Card import *
from Visitor import *
from typing import List
import random
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
class Game:

  def __init__(self, visitors_list: List[Visitor], cards_num: int = 5) -> None:

    self._player_turn: int = 0

    #cards-open a new class for this (DeckCards)
    self._load_cards()

    #players 
    self._players_positions = visitors_list
    #players card init
    for v in self._players_positions:
      cards = [card for card in self._remove_random_element(self._opposide_cards)]
      v.give_cards(cards)


  def add_cards_on_board(self, cards: List[Card] , player: Visitor) -> Exception | None:
    #Check that is the plater turn
    if (self._players_positions[self._player_turn] != player):
      raise Exception("Please wait for your trun")
    

    #validate that the player have that cards
    self._is_subarray(cards, player.cards)

    #Validate that the player make a legal move...

    #Append cards
    self._board_cards.append(cards)

    #check if the player end his deck...

    #Next player turn
    self._player_turn = (self._player_turn + 1) % len(self._players_positions)
    

  def draw_card(self):
    #Check if there is remain cards
    if self._opposide_cards:
      self._opposide_cards, self._opposide_cards = self._board_cards[1:], [self._opposide_cards[0]]
    #Remove a random card
    return self._remove_random_element(self._opposide_cards)

  def _load_cards(self) -> None:
      self._opposide_cards = [Card(c) for c in cards]
      card = self._remove_random_element(self._opposide_cards, (0, 35))
      self._board_cards = [card]
      
  
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

  def _is_subarray(self, arr1, arr2):
      """
      Check if arr1 is a subarray of arr2 (order doesn't matter).

      Parameters:
      - arr1: The potential subarray.
      - arr2: The array to check for the subarray.

      Returns:
      - True if arr1 is a subarray of arr2, False otherwise.
      """
      set_arr1 = set(arr1)
      set_arr2 = set(arr2)

      return set_arr1.issubset(set_arr2)

    
