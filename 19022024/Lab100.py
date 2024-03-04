class Car:
    color = None
    model = None

    def car_details(self):
        print("Your car details is", self.color, self.model)

car_color = input("Enter the car color:")
car_model = input("Enter the car model:")

car_obj_ref = Car()
car_obj_ref.color = car_color
car_obj_ref.model = car_model

car_obj_ref.car_details()