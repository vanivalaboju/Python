class Mul_Param:
    name = None  # Class Variable
    def print_information(self, first_name, last_name, age):
        a = 10  # Local Variable
        print("Your name is ", first_name, last_name, age)
        print(self.name)


obj_ref = Mul_Param()
obj_ref.print_information("vani", "valaboju", 34)