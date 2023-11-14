from .Visitor import Visitor
from .Card import Card
from .DeckCards import DeckCards
from typing import List


class Game:
  def __init__(self, visitors_list: List[Visitor], deck_cards: DeckCards, cards_num: int = 5) -> None:

    self._player_turn: int = 0
    #The cards in the game
    self._deck_cards = deck_cards
    #players 
    self._players_positions = visitors_list
    #players card init
    for v in self._players_positions:
      cards = self._deck_cards.draw_n_cards(cards_num)
      v.give_cards(cards)


  def add_cards_on_board(self, cards: List[Card] , player: Visitor) -> Exception | None:
    #Check that is the plater turn
    self._is_player_turn(player)
    

    #validate that the player have that cards
    self._is_subarray(cards, player.cards)

    #Validate that the player make a legal move...

    #Append cards
    self._deck_cards.append_cards(cards)

    #check if the player end his deck...

    #Next player turn
    self._next_player()
    
  
  def draw_card(self, visitor:Visitor):
    card = self._deck_cards.draw_card()
    visitor.add_cards([card])
    return card

  def _is_player_turn(self, visitor:Visitor) -> None | Exception:
    if (self._players_positions[self._player_turn] != visitor):
      raise Exception("Please wait for your trun")

  def _next_player(self):
    self._player_turn = (self._player_turn + 1) % len(self._players_positions)


  def _is_subarray(self, arr1, arr2):
      """
      Check if89 arr1 is a subarray of arr2 (order doesn't matter).

      Parameters:
      - arr1: The potential subarray.
      - arr2: The array to check for the subarray.

      Returns:
      - True if arr1 is a subarray of arr2, False otherwise.
      """
      set_arr1 = set(arr1)
      set_arr2 = set(arr2)

      return set_arr1.issubset(set_arr2)

    
