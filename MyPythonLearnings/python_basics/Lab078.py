# class and objecys in python
# class - Attributes and behaviour
# person -> object vani, tapasya, aravind, athulith

class Person:
    # Attributes  -> Data members
    name = None
    age = None
    id = None
    phone_no = None

    # Behaviour -> Methods(not the functions)

    def talk(self):
        print("I cam talk")

    def another(self):
        print("I am a Method")

    def sleep(self, name):
        print("I am a Method!!")
        print("Sleep", name)

    def walk(self):
        return "I am walking"
def anotherf():
    print("I am f(n)")


# Objects - ClassName()
shreeram = Person()
shreeram.name= "Sheeram"
print(shreeram.name)
shreeram.talk() # This belong Shreeram

pramod = Person()



amit = Person()
# nothing is THERE, SO CLEAN THE MEMEMORY
# exit the program

