# Encapsulation - bind the data v and methods(hide the important variables)
# Data members / Class variable -
# Functions - they are closed within a single blueprint
# Wrapping or binding the data variables with the methods
# we cant access protected and private variables outside like public
#By using different methods we can access private and protected variables

class Car:
    name = None # password = "123"
    # 3 different tyes of Data Members / class variables
    def __init__(self):  # __ private in nature
        self.public_var = "public"  # public - Anyone can access it
        self._protected_var = "protected123"
        self.__private_var = "pass@123"
        self.__password = "pass@123"

    def _protected_method(self):
            print("Protected!")

    def __private_method(self):
            print("Protected!")
            print()

    def printName(self):
            print("I am allowed to use the private variable becz I am in class " + self.__password)

xuv = Car()
xuv.printName()

# lambo= Car("Lambo")
# lambo.printName()

print(xuv.public_var)
# print(xuv.__password)
# print(xuv.printName())


