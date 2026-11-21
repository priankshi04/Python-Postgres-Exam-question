def f1():
    x = 1

    def g():
        print(x)
        x = 2

    g()


def f2():
    try:
        return int("12a")
    except (ValueError, TypeError) as e:
        return type(e).__name__
    else:
        return "else"
    finally:
        print("f2 finally")


def f3(d, k, i):
    try:
        return d[k][i]
    except LookupError as e:
        return type(e).__name__


def f4():
    try:
        raise ValueError("a")
    except ValueError:
        raise TypeError("b") from None


def f5():
    assert 1 + 1 == 3, "math"


def rec(n):
    return rec(n + 1)


tests = [
    f1,
    f2,
    lambda: f3({"a": [1]}, "a", 5),
    lambda: f3({}, "z", 0),
    f4,
    f5,
    lambda: rec(0),
    lambda: undefined_name,
    lambda: next(iter([])),
    lambda: [].pop(),
    lambda: {}["k"],
    lambda: int(None),
    lambda: "a" + 1,
    lambda: (1, 2).append(3)
]

for t in tests:
    try:
        print("ok", t())
    except Exception as e:
        print(type(e).__name__)


try:
    f4()
except TypeError as e:
    print(e.__cause__, e.__suppress_context__, type(e.__context__).__name__)


print(
    issubclass(KeyError, LookupError),
    issubclass(RecursionError, RuntimeError),
    issubclass(UnboundLocalError, NameError),
    issubclass(KeyboardInterrupt, Exception),
    issubclass(ZeroDivisionError, ArithmeticError),
    issubclass(StopIteration, Exception)
)


#OUTPUT
UnboundLocalError
f2 finally
ok ValueError
ok IndexError
ok KeyError
TypeError
AssertionError
RecursionError
NameError
StopIteration
IndexError
KeyError
TypeError
TypeError
AttributeError
None True ValueError
True True True False True True

Process finished with exit code 0