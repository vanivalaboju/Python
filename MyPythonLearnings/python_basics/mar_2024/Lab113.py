# To handle the exception
# try and except block
# try -> try the code
# except = execute except code (if problem try)

a = int(input("Enter num1\n"))
b = int(input("Enter num2\n"))
try:
    c = a / b  # ZeroDivisionError: division by zero
    print("Div is ", c)
except Exception as e:
    print(e)
    print("Zero Division, please dont use b as zero!")
print("This is Important message that we need show to user!")
