class Loginpage:
    email = None
    password = None

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def loginconfirm(self):
        if self.password == "pass1234":
            print("Login success")
        else:
            print("Invalid User")

sandy = Loginpage("abc@abc.com", "pass1234")
sandy.loginconfirm()