def singleton(cls):
    instance = None

    def get(*a, **k):
        nonlocal instance
        if instance is None:
            instance = cls(*a, **k)
        return instance

    return get


def add_repr(cls):
    def __repr__(self):
        fields = ", ".join(f"{k}={v!r}" for k, v in vars(self).items())
        return f"{cls.__name__}({fields})"

    cls.__repr__ = __repr__
    return cls


@singleton
class Config:
    def __init__(self, name="default"):
        self.name = name


@add_repr
class Pt:
    def __init__(self, x, y):
        self.x, self.y = x, y


a = Config("one")
b = Config("two")

print(a is b, a.name, type(Config).__name__)

try:
    isinstance(a, Config)
except TypeError as e:
    print("TypeError:", e)

print(Pt(1, 2), [Pt(3, 4)])


class Sub(Pt):
    pass


print(Sub(5, 6))

try:
    class Sub2(Config):
        pass
except TypeError as e:
    print("TypeError:", e)

print(Config.__name__)

OUTPUT
True one function
TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union
Pt(x=1, y=2) [Pt(x=3, y=4)]
Pt(x=5, y=6)
TypeError: function() argument 'code' must be code, not str
get

Process finished with exit code 0