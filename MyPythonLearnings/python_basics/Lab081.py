class Calculator:
    def sum(self,a,b):
        return a + b

    def sub(self, a, b):
            return a - b

    def mul(self, a, b):
            return a * b

    def div(self, a, b):
            return a / b

object_ref = Calculator()
r1 = object_ref.sum(3, 4)
r2 = object_ref.div(20,20)
r3 = object_ref.sub(9,6)
print(r1)
print(r2)
print(r3)