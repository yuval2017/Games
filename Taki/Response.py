class Response:
  def __init__(self, err_message = None, ret_obj = None) -> None:
    self._err_message = err_message
    self._ret_obj = ret_obj

  @classmethod
  def init_with_error(cls, err_message):
    cls(err_message = err_message)
  
  @classmethod
  def init_with_obj(cls, obj):
    cls(ret_obj = obj)

  def err_accure(self):
    return self._err_message is not None
  
  