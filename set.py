s = {10, 20, 30, "xyz"}
print(s)
print(type(s))

s.update([88, 99])
print(s)

# print(s[0])

s.remove(10)
print(s)

# Frozen set
"""
Frozen set allows only to navigate through the set and retrieve the elements
"""
s = {1, 2, 3, 4, 7, 8}
f = frozenset(s)
f.remove(2)