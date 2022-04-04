#Creation of String

s="Welcome to Python learnings"
print(s)

#index returns the value at 2
print(s[2])

#to print same string multiple times
print(s*3)

#To gvive length of thye string
print(len(s))


#String Slicing
print(s[0:3])

print(s[0:])

s1="Sakshi Shetty"
print(s1[-3:-1])

#Step value
print(s[0:8:2])

#providing negative value means will reverse the string
print(s[::-1])

#strip to remove spaces
s2="""Welcome to the course"""
print(s2.strip())
print(s2.lstrip())

#Returns the index
print(s2.find("com",0,8))

#Returns the count
print(s2.count("e"))

#To replace value with
print(s2.replace("Welcome","Starting"))




