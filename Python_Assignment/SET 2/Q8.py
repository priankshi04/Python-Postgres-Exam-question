class Shape:
    sides = 0
    registry = []

    def __init_subclass__(cls, **kw):
        super().__init_subclass__(**kw)
        Shape.registry.append(cls.__name__)

    @classmethod
    def make(cls, *args):
        print("make", cls.__name__)
        return cls(*args)

    @staticmethod
    def helper(x):
        return x * 2

    def info(self):
        return f"{type(self).__name__}:{self.sides}"


class Tri(Shape):
    sides = 3

    def __init__(self, a=1):
        self.a = a


class Sq(Shape):
    sides = 4

    @classmethod
    def make(cls, *args):
        print("Sq.make")
        return super().make(*args)

    @staticmethod
    def helper(x):
        return Shape.helper(x) + 1


t = Tri.make(5)
s = Sq.make()

print(t.a, t.info(), s.info())
print(Shape.registry)
print(Tri.helper(3), Sq.helper(3), s.helper(3))

m = t.info
print(m.__self__ is t, m.__func__ is Shape.info)

f = Shape.info
print(f(s))

try:
    Sq.make(1)
except TypeError:
    print("TypeError")

print(Tri.make.__self__ is Tri, Sq.make.__self__ is Sq)
#SOLUTION
make Tri
Sq.make
make Sq
5 Tri:3 Sq:4
['Tri', 'Sq']
6 7 7
True True
Sq:4
Sq.make
make Sq
TypeError
True True

Process finished with exit code 0
