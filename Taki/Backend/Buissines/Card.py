class Card:
  def __init__(self, type: str) -> None:
    self._type = type

  @property
  def type(self) -> str:
    return self._type
  
  @type.setter
  def type(self, new_type: str) -> None:
    self._type = new_type
    
  def __str__(self) -> str:
    return self._type