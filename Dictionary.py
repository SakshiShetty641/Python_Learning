dict1 = {1: "xyz", 2: "pqr", 3: "ijk", 4: "abx"}
print(dict1)


print(dict1.values())
print(dict1.keys())

print(dict1[3])

#Python function delete -> del
del dict1[4]
print(dict1)

"""For Loops"""
k=dict1.keys()
for i in k:
    print(i)

w=dict1.values()
for j in w:
    print(j)

