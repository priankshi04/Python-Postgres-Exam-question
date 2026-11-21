class Animal:
    sound = "..."
    legs = 4

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says {self.sound}"

    def describe(self):
        return f"{self.speak()} on {self.legs} legs"


class Bird(Animal):
    legs = 2
    sound = "tweet"

    def fly(self):
        return f"{self.name} flies"


class Penguin(Bird):
    def __init__(self, name, colony="south"):
        super().__init__(name)
        self.colony = colony

    def fly(self):
        return f"{self.name} cannot fly; " + super().fly().replace("flies", "swims")


class Dog(Animal):
    sound = "woof"

    def speak(self):
        return super().speak().upper()


class Robot:
    legs = 2

    def speak(self):
        return "beep"

    def describe(self):
        return "robot " + self.speak()


zoo = [Animal("generic"), Penguin("pingu"), Dog("rex"), Robot()]

for z in zoo:
    print(z.describe())

print(Penguin("p").fly())
print([getattr(z, "fly", lambda: None)() for z in zoo])

p = Penguin("p2")
p.sound = "honk"

print(p.speak(), Penguin.sound, Bird.sound, p.legs)

print(
    Penguin.__mro__ == (Penguin, Bird, Animal, object),
    issubclass(Penguin, Animal),
    hasattr(Robot, "name")
)

OUTPUT
generic says ... on 4 legs
pingu says tweet on 2 legs
REX SAYS WOOF on 4 legs
robot beep
p cannot fly; p swims
[None, 'pingu cannot fly; pingu swims', None, None]
p2 says honk tweet tweet 2
True True False

Process finished with exit code 0
