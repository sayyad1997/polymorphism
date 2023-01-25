class car:
    def type(self):
        print("there are different types of cars")

    def milage(self):
        print("according to the company of the car milage is vary")

class tata(car):
    def type(self):
        print("type of car will be petrol")
    def milage(self):
        print("23km per hour")

class mahindra(car):
    def type(self):
        print("type of car will be diesel")
    def milage(self):
        print("25km per hour")



def model(cars):
    cars.type()
    cars.milage()
vehicle=car()
car_tata=tata()
car_mahindra=mahindra()
model(vehicle)
model(car_tata)
model(car_mahindra)