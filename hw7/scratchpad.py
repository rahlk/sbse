class Thing():
  id = 0
  def __init__(self, **entries): 
    self.id = Thing.id = Thing.id + 1
    self.__dict__.update(entries)
    