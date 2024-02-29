# single inheritance - 80%
# Multiple
# Multi level
# Hybrid
# Heri

# API, Web Automation - 80% -> Single

# Multilevel Inheritance
class GrandParent:
    def grandparent_method(self):
        return "Grandparent method"
class Parent(GrandParent):
    def parent_method(self):
        return "Parent method"
class Child(Parent):
    def Child_method(self):
        return "child method"

ch = Child()
print(ch.grandparent_method())
print(ch.parent_method())
print(ch.Child_method())

# parent ref = parent object()
p = Parent()
print(p.parent_method())
print(p.grandparent_method())

gp = GrandParent()
print(gp.grandparent_method())
