# using same defination for different datatypes
def sum_of_num(a, b):
    return a + b


result = sum_of_num(3, 4)
print(result)

result1 = sum_of_num(22.4, 49.89)
print(result1)

result2 = sum_of_num("Pramod", "Dutta") # concatenate of 2 strings
print(result2)

# TypeError: can only concatenate str (not "int") to str
#result3 = sum_of_num("Pramod", 123)
#print(result3)

a = None
print(a)