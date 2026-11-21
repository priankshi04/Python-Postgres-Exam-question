import copy


class Wheel:
    def __init__(self, n):
        self.n = n


class Engine:
    def __init__(self):
        self.hp = 100


class Car:
    def __init__(self, name):
        self.name = name
        self.engine = Engine()
        self.wheels = [Wheel(i) for i in range(2)]


class Garage:
    def __init__(self, *cars):
        self.cars = list(cars)

    def add(self, car):
        self.cars.append(car)
        return self


class Driver:
    def drive(self, car):
        car.engine.hp -= 10
        return car.engine.hp


c1, c2 = Car("a"), Car("b")
g1, g2 = Garage(c1), Garage(c1, c2)

print(c1.engine is c2.engine, g1.cars[0] is g2.cars[0])

d = Driver()

print(d.drive(c1), d.drive(g2.cars[0]), c1.engine.hp, c2.engine.hp)

del g1

print(c1.name, len(g2.cars))

g3 = copy.copy(g2)
g3.add(Car("c"))

print(len(g2.cars), len(g3.cars), g3.cars[0] is c1)

g4 = copy.deepcopy(g2)
g4.cars[0].engine.hp = 0

print(c1.engine.hp, g4.cars[0].engine.hp, g4.cars[0] is c1, g4.cars[0].name)

print(c1.wheels is c2.wheels, c1.wheels[0] is not c2.wheels[0],
      len({id(w) for car in (c1, c2) for w in car.wheels}))


#OUTPUT
False True
90 80 80 100
a 2
3 3 True
80 0 False a
False True 4

Process finished with exit code 0