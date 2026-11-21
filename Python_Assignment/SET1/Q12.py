class Token:
    _cache = {}

    def __new__(cls, v):
        print("new", v)
        if v not in cls._cache:
            cls._cache[v] = super().__new__(cls)
        return cls._cache[v]

    def __init__(self, v):
        print("init", v)
        self.v = v
        self.hits = getattr(self, "hits", 0) + 1


a = Token("x")
b = Token("x")
c = Token("y")

print(a is b, a is c, a.hits, c.hits)


class Weird:
    def __new__(cls):
        return 42

    def __init__(self):
        print("init Weird")


class Child(Token):
    pass


d = Child("x")
print(type(d).__name__, d is a, Weird())
#SOLUTION
new x
init x
new x
init x
new y
init y
True False 2 1
new x
Token True 42

Process finished with exit code 0
