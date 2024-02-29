# Single Inheritance
class Father:
    __private_villa = "GOA"
    gold = 5
    def drive_car(self):
        print("Lambo")
    def threeBHKFlat(self):
        print("3BHK Flat")
    def private_vill_access(self,is_my_daughter):
        print(self.__private_villa)
class Daughter(Father):  # single inheritance whatever father has daughter will get all properties
    pass
vani = Daughter()
vani.drive_car()
vani.threeBHKFlat()
print(vani.gold)
# vani.__private_var() - daughter doesnt access private variable of father
vani.private_vill_access(True)

mm = Father()
mm.drive_car()
mm.threeBHKFlat()

