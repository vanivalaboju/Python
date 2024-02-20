browser = str (input("Enter the browser name\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("chrome code is executed!")
    case "firefox":
        print("FF code is executed!")
    case "safari":
        print("safari code is executed!")
    case "brave":
        print("Brave code is executed!")