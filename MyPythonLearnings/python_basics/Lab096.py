# single Inheritance
# Multi level

class GF:
    def __init__(self):
        print("Automatically called when object is created")
    name = "vani"
    def home(self):
        self.name2 = "vani"
        print("5BHK")
class Father(GF):
    def home2(self):
        print("Warangal")
class Daughter(Father):
    def home3(self):
        print("Hyderabad")

vani = Daughter()
vani.home()
vani.home2()
vani.home3()
