# Multiple Inheritance

# F,M -> D
class Father:
    def father_money(self):
        return "5"
    def home(self):
        return "This is from the father"
class Mother:
    def mother_money(self):
        return "2"
    def home(self):
        return "This is from the mother"
class Daughter(Mother,Father):
    pass

# class Daughter(Father,Mother):
#     def home(self):
#         return "This is from daughter"
daughter = Daughter()
print(Daughter.mro()) # MRO ->method resolution order
print(daughter.home())
print(daughter.father_money())
print(daughter.mother_money())

