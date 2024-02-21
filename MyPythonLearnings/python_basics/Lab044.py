# *args and **kargs
def f1(a=1,b=1,c=1):
    return a + b + c
print(f1())
print(f1(5))
print(f1(1,2))
print(f1(1,2,3))
print(f1(a=10, b=20, c=30))

# r = f1(c=1, a=2, b=90)
# print(r)

# *args
def sum(a, b, c, d, e): # instead of using multiple args we can use *args
    return a + b + c + d + e
# r = sum(1, 2, 3) # in this how many args we can take it take that many values not less not more args
r = sum(1, 2, 3, 4, 5)
print(r)

def print_argument(*args):
    for i in args:
        print(i,end=" ")
print_argument(1) # we can take as much as args because we are using *args
print_argument(1,2)
print_argument(1,2,3)
print_argument(1,2,3,4)

