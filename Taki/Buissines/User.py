from Visitor import *
class User(Visitor):
  def __init__(self,id ,user_name) -> None:
    super().__init__(id)
    self._user_name = user_name
