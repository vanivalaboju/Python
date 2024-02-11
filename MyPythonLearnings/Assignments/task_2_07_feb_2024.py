# Write a python program to calculate the area of a circle given its radius using the formula
# area = pi*r**2


radius = float(input("Enter the radius of the circle:"))
pi = 3.14
area = pi * radius ** 2
print("The area of the circle is:", area)

""" Create a program that takes two numbers as input
 and prints whether the first number is greater than
 less than or equal to the second number"""
n1 = input("Enter the first number:")
n2 = input("Enter the second number:")
if n1 > n2 :
    print("The first number is greater than second number")
elif n1 < n2:
    print("The first number is less than second number")
else:
    print("The first number is equals to second number")

# Develop a python script that calculates the square and cube of a given number

num = int(input("enter the number to calculate square of a given number:"))
square = num ** 2
print("The square of a given number is:",square)
num2 = int(input("enter the number to calculate cube of a given number:"))
cube = num2 ** 3
print("The cube of a given number is:",cube)