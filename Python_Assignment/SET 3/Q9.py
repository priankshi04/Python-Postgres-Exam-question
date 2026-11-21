class Vehicle:
    count = 0

    def __init__(self, wheels=4):
        print("Vehicle", wheels)
        self.wheels = wheels
        type(self).count += 1


class Bike(Vehicle):
    def __init__(self):
        print("Bike")
        self.gears = 21


class Car(Vehicle):
    def __init__(self, doors=4):
        super().__init__()
        print("Car", doors)
        self.doors = doors


b = Bike()
c = Car(2)
d = Car()

print(Vehicle.count, Bike.count, Car.count)
print(hasattr(b, "wheels"), c.wheels, vars(c))

try:
    print(b.wheels)
except AttributeError as e:
    print("AttributeError:", e)

    OUTPUT
Bike
Vehicle 4
Car 2
Vehicle 4
Car 4
0 0 2
False 4 {'wheels': 4, 'doors': 2}
AttributeError: 'Bike' object has no attribute 'wheels'

Process finished with exit code 0
