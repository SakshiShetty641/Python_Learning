list = ["India", "USA", "UK"]
print(list)

list.append("Europe")
print(list)

del list[1]
print(list)

list.insert(1, "Brazil")
print(list)


set = {"India", "USA", "UK"}
print(set)

set.update(["Europe"])
print(set)


set.remove("Europe")
print(set)