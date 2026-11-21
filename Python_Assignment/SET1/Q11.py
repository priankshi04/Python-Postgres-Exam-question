from abc import ABC, abstractmethod


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def label(self):
        ...

    def describe(self):
        return f"{self.label()}={self.area:.1f}"


class Square(Shape):
    def __init__(self, a):
        self.a = a

    @property
    def area(self):
        return self.a ** 2


class LabelledSquare(Square):
    def label(self):
        return "sq"


class Disc:
    def __init__(self, r):
        self.r = r

    area = property(lambda self: 3.0 * self.r ** 2)

    def label(self):
        return "disc"

    describe = Shape.describe


class Gallery:
    def __init__(self, *shapes):
        self.shapes = shapes

    def total(self):
        return sum(s.area for s in self.shapes)

    def report(self):
        return ", ".join(s.describe() for s in self.shapes)


def attempt(n, thunk):
    try:
        print(n, thunk())
    except TypeError as e:
        print(n, "TypeError")


attempt(1, lambda: Shape())
attempt(2, lambda: Square(2))
attempt(3, lambda: LabelledSquare(2).describe())

g = Gallery(LabelledSquare(2), Disc(1))

attempt(4, lambda: (g.total(), g.report()))
attempt(5, lambda: isinstance(Disc(1), Shape))
attempt(6, lambda: (sorted(Square.__abstractmethods__),
                    LabelledSquare.__abstractmethods__))
attempt(7, lambda: Shape.describe(Disc(2)))
#SOLUTION
1 TypeError
2 TypeError
3 sq=4.0
4 (7.0, 'sq=4.0, disc=3.0')
5 False
6 (['label'], frozenset())
7 disc=12.0

Process finished with exit code 0
