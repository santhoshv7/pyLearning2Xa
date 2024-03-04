class Person:
    name = None
    age = None
    id = None
    phone_no = None

    def talk(self):
        print("I can talk")

    def eat (self):
        print ("I can eat")

    def sleep (self):
        print ("I can sleep")

def standalone():
    print("I am a standalone function")

santhosh = Person()
santhosh.name = "santhosh"
print(santhosh.name)
malar = Person()
santhosh.talk()