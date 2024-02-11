# Create a program that determines whether a given year is a leap year
year = int(input("enter the year:"))
if (year % 4 == 0) or (year % 400 == 0 and year % 100 !=0):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")

# Write a program that classifies a triangle based on its side lengths
# Use an if-else statement to classify the triangle
# 3 inputs side1,side2,side3
side1 = int(input("enter the first side of a triangle:"))
side2 = int(input("enter the second side of a triangle:"))
side3 = int(input("enter the third side of a triangle:"))
if side1 == side2 == side3:
    print("The triangle is Equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3 :
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")


# write a python program to find a factorial of a number
import math

n = int(input("enter the number to find factorial of a number:"))
f = math.factorial(n)

print("The factorial of a number is:",f)
