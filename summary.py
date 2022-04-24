
#Same memory location - same value means same memory location
a=10
b=10
print(id(a))
print(id(b))

#Different values means different memory location
c=10
d=20
print(id(c))
print(id(d))