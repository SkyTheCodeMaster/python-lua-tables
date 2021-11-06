class Table(dict):
  def __getattr__(self,x):
    return self.get(x,None)
  def __setattr__(self,k,v):
    if type(v) is dict:
      temp = Table()
      for x,y in v.items():
        temp[x] = y
      self[k] = temp
    else:
      self[k] = v
