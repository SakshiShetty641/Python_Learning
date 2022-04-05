"""IF it has same value then it allocates to the same memory location"""

a=10;
b=10;
print(id(a))
print(id(b))

c=True;
d=True;
print(id(c))
print(id(d))

"""Different memory location"""
g=True
h=False
print(id(g))
print(id(h))
