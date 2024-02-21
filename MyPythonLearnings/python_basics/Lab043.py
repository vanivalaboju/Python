""" Function - Block of code which can be executed
    1.They can return something
    2.They cant return ->non return
    3.They have parameters
    4.They dont have parameters / arguments """

# Define -> call
def say_hello():  # No return type and no parameter / argument
    # write the code
    print("welcome to function concepts:")
say_hello()

def say_hello_arg(name): # No return type and with one argument
    # write the code
    print("Hello",name)
say_hello_arg("Harika")

def say_hello_args(name,age): # No return type and with multiple argument & diif datatype
    # write the code
    print("Hello",name,age)
say_hello_args("Harika",34)
say_hello_args(123,True)

# No return type with default argument
def say_hello_arg_default(name="Harika"):
    # Write the code
    print("Hello",name)
say_hello_arg_default()
say_hello_arg_default(name="Tapasya")
say_hello_arg_default("Athulith")

# function with argument and return type
def sum_number_argument_ret(a,b):
    return a + b
result = sum_number_argument_ret(3,4)
result1 = sum_number_argument_ret("vani","Aravimd")
result2 = sum_number_argument_ret(a=10, b=90)
# result3 = sum_number_argument_ret(a="Harika",34)
print(result)
print(result1)
print(result2)








