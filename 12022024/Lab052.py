browser =input("Enter the browser name\n")
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code is executed")
    case "firefox":
        print("Firefox code is executed")
    case _:
        print("browser not found")