class Table(dict):
  def __init__(self,d:dict=None):
    if d:
      for k,v in d.items():
        self.__setattr__(k,v)
  def __getattr__(self,x):
    return self.get(x,None)
  def __getitem__(self,x):
    return self.get(x,None)
  def __setattr__(self,k,v):
    if type(v) is dict:
      temp = Table()
      for x,y in v.items():
        temp[x] = y
      self[k] = temp
    else:
      self[k] = v
