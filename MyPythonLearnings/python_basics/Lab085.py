"""  to create a class keyword name as class
class name should be capital letter first one"""

class Person:
    # Class Variables/ Instance variables
    name = "vani"
    age = None

# self is used as instance of Person class
# to access class variables name and age we write self in function

    def walk(self):
        a = 10  # Local variable
        print("Hi your name is ", self.name)
        print("Hi your age is ", self.age)
        print(a)

vani = Person()  # to create a object
vani.walk()     # calling function

"""if i change the object also same name vani is printing output
 so to change the values of name and age 
 based on obj we created we have to use constructor(). """
Tapasya = Person()
Tapasya.walk()