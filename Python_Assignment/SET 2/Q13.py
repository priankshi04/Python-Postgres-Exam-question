trace = []


class Engine:
    def __init__(self, hp):
        self.hp = hp

    def start(self):
        return f"engine {self.hp}hp"

    def stop(self):
        return "engine stop"


class Car:
    wheels = 4

    def __init__(self, hp):
        self.engine = Engine(hp)

    def __getattr__(self, name):
        trace.append(name)
        return getattr(self.engine, name)

    def stop(self):
        return "car stop"


c = Car(90)

print(c.wheels, trace)
print(c.start(), trace)
print(c.stop(), trace)
print(c.hp, trace)

try:
    c.fuel
except AttributeError as e:
    print("AttributeError:", e)

print(hasattr(c, "engine"), hasattr(c, "doors"), trace)

c.hp = 120
print(c.hp, c.engine.hp, trace)

d = Car.__new__(Car)
trace.clear()

try:
    d.start()
except RecursionError:
    print("RecursionError", trace[:3], len(trace) > 100)
#SOLUTION
4 []
engine 90hp ['start']
car stop ['start']
90 ['start', 'hp']
AttributeError: 'Engine' object has no attribute 'fuel'
True False ['start', 'hp', 'fuel', 'doors']
120 90 ['start', 'hp', 'fuel', 'doors']
RecursionError ['start', 'engine', 'engine'] True

Process finished with exit code 0
