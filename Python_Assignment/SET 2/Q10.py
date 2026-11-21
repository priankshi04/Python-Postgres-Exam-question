class Base:
    def __init__(self):
        print("Base.init")
        self.log = ["Base"]


class Left(Base):
    def __init__(self):
        print("Left.init")
        Base.__init__(self)
        self.log.append("Left")


class Right(Base):
    def __init__(self):
        print("Right.init")
        super().__init__()
        self.log.append("Right")


class Both(Left, Right):
    def __init__(self):
        print("Both.init")
        super().__init__()
        self.log.append("Both")


b = Both()

print(b.log)
print([c.__name__ for c in Both.__mro__])


class Mixin:
    def hello(self):
        return "mixin-" + super().hello()


class Core:
    def hello(self):
        return "core"


class X(Mixin, Core):
    pass


class Y(Core, Mixin):
    pass


class Z(Mixin):
    pass


print(X().hello())
print(Y().hello())

try:
    Z().hello()
except AttributeError as e:
    print("AttributeError:", e)
#SOLUTION
Both.init
Left.init
Base.init
['Base', 'Left', 'Both']
['Both', 'Left', 'Right', 'Base', 'object']
mixin-core
core
AttributeError: 'super' object has no attribute 'hello'

Process finished with exit code 0
