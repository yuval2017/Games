
from Card import *
from Visitor import *
from typing import List

class Game:

  def __init__(self, visitors_list: List[Visitor]) -> None:
    #players
    self._players_positions: List[Visitor] = visitors_list
    self._player_turn: int = 0
    #cards-open a new class for this (DeckCards)
    self._board_cards: List[Card] = []
    self._opposide_cards: List[Card] = []
    # create all cards

    #give each player card
    pass

  def put_card(self, card: Card, player: Visitor) -> Exception | None:
    #Check that is the plater turn
    if (self._players_positions[self._player_turn] != player):
      raise Exception("Please wait for your trun")
    
    #Validate card

    #Put card

    #next player turn
    self._player_turn = (self._player_turn + 1) % len(self._players_positions)
    pass

  def shuffle_cards(self) -> None:
    pass



    
