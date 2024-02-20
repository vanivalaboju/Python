# program to find the maximum between 3 numbers
num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
num3 = int(input("enter num3"))
""" max_num = max(num1,num2,num3)
print(max_num) """
if num1 > num2 and num1 > num3:
    print("max is num1:12",num1)
elif  num2 > num1 and num2 > num3:
    print("max is num2:",num2)
else:
    print("max is num3:", num3)
