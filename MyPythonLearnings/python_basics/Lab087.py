# Web Automation - Selenium

# Page - you are going automate
class VWOLoginPage:
    email = None
    password = None

    def __init__(self,email,password):
        self.email = email
        self.password = password
    def login_confirm(self):
        if self.password == "pass123":
            print("you are allowed to enter")
        else:
            print("Invalid user")
vani = VWOLoginPage("vani.v3509@gmail.com","123")
vani.login_confirm()

print(" ------ ")

Athulith = VWOLoginPage("athulith.14@gmail.com","pass123")
Athulith.login_confirm()

# id means their memory where they are stored references
print(id(vani))
print(id(Athulith))