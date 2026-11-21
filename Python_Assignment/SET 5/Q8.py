from abc import ABC, abstractmethod


class Plugin(ABC):
    @classmethod
    @abstractmethod
    def key(cls):
        ...

    @abstractmethod
    def run(self, x):
        return f"base({x})"


class Upper(Plugin):
    @classmethod
    def key(cls):
        return "up"

    def run(self, x):
        return super().run(x).upper()


class Half(Plugin):
    @classmethod
    def key(cls):
        return "half"


class Virtual:
    def run(self, x):
        return "virtual"


Plugin.register(Virtual)

print(Upper().run("a"), Upper.key())

try:
    Half()
except TypeError:
    print("TypeError")

print(sorted(Plugin.__abstractmethods__), sorted(Half.__abstractmethods__))
print(isinstance(Virtual(), Plugin), issubclass(Virtual, Plugin))
print([c.__name__ for c in Virtual.__mro__])

try:
    Plugin()
except TypeError:
    print("TypeError")

#OUTPUT
BASE(A) up
TypeError
['key', 'run'] ['run']
True True
['Virtual', 'object']
TypeError

Process finished with exit code 0