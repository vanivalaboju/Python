# conversion of data types int to float and float to int
a = 23
c = 12.9
b = float(a)
d = int(c)
print(type(a))
print(type(c))
print(type(b))
print(type(d))

# Reverse of a string
name = input("Enter a name")  # naman
reverse = ("")
for i in range(len(name) - 1, -1):
    reverse = name[i] + reverse
print(reverse)