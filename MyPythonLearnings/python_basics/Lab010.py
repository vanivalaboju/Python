# In a format string if i change value of variable then entire output changes
# In below example if i change num = 90 then table 0f 90 is printed
num = 2
print(f"{num}x1={num}")
print(f"{num}x2={num*2}")
print(f"{num}x3={num*3}")
print(f"{num}x4={num*4}")
print(f"{num}x5={num*5}")
print(f"{num}x6={num*6}")
print(f"{num}x7={num*7}")
print(f"{num}x8={num*8}")
print(f"{num}x9={num*9}")
print(f"{num}x10={num*10}")

# we can also use .format
for b in range(1,11):
        print("2x{}={}".format(b,2*b))
# we can also give more arguments dynamically gives values in it
print("my name is {} and my age is {}".format("Harika",34))
