class MyClass:
    def __init__(self):
        self.name = "vani"
    def public_func(self):
        print("public function()")
    def __private_func(self):
        print("This is private")
    def public_fn_private(self):
        self.__private_func()
# Security -> Not everyone can access your variables,f(n)

a = MyClass()
a.public_func()
# a.__private_func() - Not allowed
a.public_fn_private()