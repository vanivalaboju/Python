# Hierarchial Inheritance
class Father:
    def home(self):
        return "This is a Father home"
class Veena(Father):
    def home(self):
        return "This is a veena home"
class Vani(Father):
    def home(self):
        return "This is a vani home"
vani = Vani()
print(vani.home())
veena = Veena()
print(veena.home())
f = Father()
print(f.home())