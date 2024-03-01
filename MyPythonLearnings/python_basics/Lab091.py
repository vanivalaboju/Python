class SecureClass:
    def submit(self):
        self.__password = "123"
        self.__username = "admin"
        self.heading = "VWO login"
chrome = SecureClass()
chrome.submit()
print(chrome.heading)