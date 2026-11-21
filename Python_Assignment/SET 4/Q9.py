class Temp:
    def __init__(self, c=0):
        self._c = 0
        self.set_c(c)

    def get_c(self):
        print("get")
        return self._c

    def set_c(self, v):
        print("set", v)
        if not isinstance(v, (int, float)):
            raise TypeError("number required")
        self._c = v

    def del_c(self):
        print("del")
        del self._c

    celsius = property(get_c, set_c, del_c, "temperature in C")

    @property
    def kelvin(self):
        return self.celsius + 273


t = Temp(20)
t.celsius += 5

print(t.kelvin)

try:
    t.kelvin = 1
except AttributeError:
    print("read-only")

try:
    t.celsius = "hot"
except TypeError as e:
    print(e)

del t.celsius

print(hasattr(t, "_c"))

try:
    t.celsius
except AttributeError:
    print("AttributeError")

print(Temp.celsius.__doc__, type(Temp.kelvin).__name__)

OUTPUT
set 20
get
set 25
get
298
read-only
set hot
number required
del
False
get
AttributeError
temperature in C property

Process finished with exit code 0
