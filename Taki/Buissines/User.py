from Visitor import *
class User(Visitor):
  def __init__(self,id ,user_name, game_position: int) -> None:
    super().__init__(id, game_position)
    self._user_name = user_name
