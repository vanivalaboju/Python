# square root of anumber
import math
num = int(input("Enter the number:"))
def sq_rt(num):
    return math.sqrt(num)
def cb_rt(num):
    return math.cbrt(num)
squareroot = sq_rt(num)
cuberoot = cb_rt(num)
print(squareroot)
print(cuberoot)