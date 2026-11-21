class Log:
    def __init__(self, name, swallow=False):
        self.name, self.swallow = name, swallow

    def __enter__(self):
        print("enter", self.name)
        return self

    def __exit__(self, et, ev, tb):
        print("exit", self.name, et.__name__ if et else None)
        return self.swallow


def f():
    with Log("A", swallow=True):
        with Log("B"):
            return "from-body"

    return "after"


def g():
    with Log("C", swallow=True):
        raise ValueError("v")

    return "after-g"


def h():
    try:
        with Log("D"):
            return "from-h"
    finally:
        print("finally-h")


def k():
    for i in range(3):
        with Log(f"L{i}"):
            if i == 1:
                continue

            if i == 2:
                break

        print("end of iteration", i)

    return "k done"


def m():
    try:
        return "try"
    finally:
        return "finally"


def n():
    try:
        raise KeyError("first")
    except KeyError:
        try:
            raise ValueError("second")
        finally:
            print("inner finally")
    finally:
        print("outer finally")


print(f())
print(g())
print(h())
print(k())
print(m())

try:
    n()
except ValueError as e:
    print(e, repr(e.__context__))


#OUTPUT
enter A
enter B
exit B None
exit A None
from-body
enter C
exit C ValueError
after-g
enter D
exit D None
finally-h
from-h
enter L0
exit L0 None
end of iteration 0
enter L1
exit L1 None
enter L2
exit L2 None
k done
finally
inner finally
outer finally
second KeyError('first')

Process finished with exit code 0