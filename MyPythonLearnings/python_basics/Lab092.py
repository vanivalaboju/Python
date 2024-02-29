class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100  # we can access dis private variable by creating public function
    def public_fn(self):
        print(self.__private_var)
    def deposit(self,amount):
        self.balance += amount
    def _withdraw(self,amount):
        self.balance -= amount
    def __show_balance(self):
        print("your bal",self.balance)
    def if_you_are_auth(self,flag):
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")
    def do_with_by_bank_manager(self,amount):
        self._withdraw(amount=amount)  # default arguments
jp_chase = BankAccount()
jp_chase.deposit(1000) # public function
jp_chase.do_with_by_bank_manager(499)  #protected func only called by d0_with_by_bank_manager method
jp_chase.if_you_are_auth(True)  # private func u will get balance only u are authenticated
jp_chase.public_fn()


