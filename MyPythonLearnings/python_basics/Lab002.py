''' python is Dynamically typed  - python determines the type of a variable
  during runtime rather than during compilation'''
age = 34
print(type(age))  # The interpreter automatically determines the type of the variable
age = "Thirty - four"
print(type(age))  # we can also reassign a variable to a different type without any issues

# print()-print function gives output to user
# print defination - print(self,*args,sep='',end='\n',file=None)
print("kathiroju family!")  # it prints output in one argument
print("Brahmam" ,"Kamala", "Aravind", "Harika", "Tapasya", "Athulith") # *args means it prints multiple arguments
print("siri","veda", "sita", sep='_')
print("siri", "veda", "sita", sep='$')  # prints $ between words
print("siri", "veda", "sita", sep='@')
print("hi", "hello", "world", sep="\n")
print("P", "y", "t", "h", "o", "n",file=None)  # it gives only spaces between character prints nothing

# Take a user input and print the details
# input means built-in function(input(*args,**kwargs)
# in input wharever we give it can print like message
name = input("Enter your name")
print("This is your name",name)
number = input(1)
print(number)

