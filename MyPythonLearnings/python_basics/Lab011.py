# How strings are stored in python
# strings are immutable meaning cannot be changed or modified
name = "Athulith"
print(len(name))
print(name[2])
# print(name[9])- string index out of range
str1 = "Hello"
print(str1)
# str1[0] = "p"- TypeError object doesn't support item assignment

# How a reverse a string in python
txt = "hello athulith"
print(len(txt))
print(txt[::-1])  # it reverse entire string
print(txt[:-1])  # except last character in string it prints remaining string
print(txt[-1])  # it only prints last character
