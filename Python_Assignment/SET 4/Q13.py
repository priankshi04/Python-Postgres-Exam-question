class Upper(str):
    def __new__(cls, v):
        print("new", v)
        return super().__new__(cls, v.upper())

    def __init__(self, v):
        print("init", v, self)


class Point(tuple):
    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))

    @property
    def x(self):
        return self[0]


u = Upper("abc")

print(u, type(u).__name__, u == "ABC", isinstance(u, str), u + "d", type(u + "d").__name__)

p = Point(1, 2)
x, y = p

print(p, p.x, y, len(p), p == (1, 2))

try:
    p.x = 5
except AttributeError:
    print("AttributeError")

p.z = 5

print(p.z, p.__dict__)

OUTPUT
new abc
init abc ABC
ABC Upper True True ABCd str
(1, 2) 1 2 2 True
AttributeError
5 {'z': 5}

Process finished with exit code 0