list=[10,20, 30, "Sakshi"]
print(list)

#Slicing, length, index
print(list[2])
print(list[0:2])
print(len(list))
print(list*2)


#To add - append
#Note - Append takes only one argument
list.append(45)
print(list)

#Also case sensitive
list.remove(30)
print(list)

#Removing by index - del -> inbuilt function
del(list[1])
print(list)

print(max(list))
print(min(list))

list.insert(2, 99)
print(list)

#Sort in ascending order
list.sort();
print(list)

#Sort in descending order
list.sort(reverse=True)
print(list)