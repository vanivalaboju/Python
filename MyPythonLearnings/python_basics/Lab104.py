class GF:
    def car(self):
        return "old car"
class F(GF):
    def car(self):
        return "honda civic"
class D(F):
    def car(self):
        return "mahindra XUV 700"
d = D()
print(d.car())
f = F()
print(f.car())
g = GF()
print(g.car())
