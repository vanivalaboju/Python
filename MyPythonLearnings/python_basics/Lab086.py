""" init is initialization dis is a special function,
which is automatically called whenever  object is created,
which means if i pass arguments like name i can set the values of name,
in python non parameter constructor not allowed ,
if i used already parameterized constructor like below ."""
class Car:

    name = None
    make = None
    model = None
    def __init__(self, o_name, o_make, o_model):
          self.name = o_name    # o_name is reference we can use any name instead of o_name
          self.make = o_make
          self.model = o_model
    def start_engine(self):
       print("Starting a car with the name " + self.name)
       print("Starting a car with the name " + self.make)
       print("Starting a car with the name " + self.model)
lambo = Car("lambo","V2","2024")
lambo.start_engine()

print(" ------ ")
# Both objects are different in name make and model
XUV = Car("XUV","V6","2023")
XUV.start_engine()
