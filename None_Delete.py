"""The difference is that x = None will free whatever it referenced but keep the name around even though
   it's just referencing None (which is a type, NoneType).
 On the other hand, del x will completely remove both the name and what it referenced."""

a= None
print(a)


b=10
del b
print(b)
