class Table(dict):
  def __getattr__(self,x):
    if x in self:
      return self[x]
    else:
      return None
  def __setattr__(self,k,v):
    if type(v) is dict:
      temp = ODict()
      for x,y in v.items():
        temp[x] = y
      self[k] = temp
    else:
      self[k] = v
