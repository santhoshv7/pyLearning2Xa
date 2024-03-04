class Car():
    name = None
    year = None
    variant = None
    speed = None

    def start_engine(self):
        print("Engine started")

    def drive(self):
        print("The car is driven")

    def stop(self):
        print("The car is stopped")

    def who_is_driving(self):
        print ("I am driving ->" + self.name)



creta_object = Car()
elevate_object =  Car()
creta_object.name = "creta"
elevate_object.name = "elevate"

creta_object.who_is_driving()
elevate_object.who_is_driving()