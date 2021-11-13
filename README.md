# python-lua-tables
Lua tables in Python

# Example usage:
```py
from luatable import Table

tbl = Table()
tbl["x"] = 5
tbl.y = 45

print(tbl) #> {'x': 5, 'y': 45}
print(tbl.x) #> 5

tbl.z = {}
tbl.z.hi = "Hi!"

print(tbl) #> {'x': 5, 'y': 45, 'z': {'hi': 'Hi!'}}
print(tbl.z.hi) #> "Hi!"

print(tbl["z"]["hi"]) #> "Hi!"
```
These function identically to Lua tables, except that metatables are not supported.
