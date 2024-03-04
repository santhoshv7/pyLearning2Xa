class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("starting a car with name" + self.name)
        print("starting a car with make" + self.make)
        print("starting a car with model" + self.model)

lambo = Car("lambo", "M3","2024")
lambo.start_engine()

creta = Car("creta", "M4", "2023")
creta.start_engine()