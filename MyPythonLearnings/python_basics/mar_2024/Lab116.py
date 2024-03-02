try:
    c = 10/0
except Exception as e:
    print(e)
# IndentationError
# SyntaxError
# ValueError
# ZeroDivisionError

# Exception -> Parent for the all exception
# Good coding and Bad coding
# If you know the exception which can come use that specific exception

# a =  int(input("Enter a number only \n"))
# ValueError -> Exp ->good coding , you know the exception
# Exception - > Bad coding practice

try:
    a = int(input("Enter a number only \n"))
except ValueError as v:
    print(v)
except Exception as e:
    print(e)
else:
    print("Else")
