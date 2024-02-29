# Multi Level Inheritance
class GF:
    def __init__(self):
        print("Automatically called when object is created")
    name = "vani"
    def home(self):
        self.name2 = "vani"
        print("5BHK")
class Father(GF):
    def home2(self):
        print("America")
class Daughter(Father):
    def home3(self):
        print("Hyderabad")
vani = Daughter()
vani.home()
vani.home2()
vani.home3()

vrb = Father()
vrb.home()
vrb.home2()
# vrb.home3() it is not allowed because it is daughter method father inherits only grandfather

shanmuk = GF()
shanmuk.home()
# shanmuk.home2() it is not allowed bcoz it only access hos method not father and daughter not access


