from contextlib import contextmanager


@contextmanager
def res(name, swallow=False):
    print("open", name)
    try:
        yield name
    except ValueError as e:
        print("handled", name, e)
        if not swallow:
            raise
    finally:
        print("close", name)


def work():
    with res("A") as a, res("B", True) as b:
        print("body", a, b)
        raise ValueError("boom")
        print("unreachable")
    return "after"


def work2():
    with res("C"):
        return "from-with"


def work3():
    try:
        with res("X"):
            with res("Y", True):
                raise ValueError("inner")
            print("continues")
            raise KeyError("k")
    except KeyError as e:
        print("caught", e)


print(work())
print(work2())
print(work3())
#SOLUTION
open A
open B
body A B
handled B boom
close B
close A
after
open C
close C
from-with
open X
open Y
handled Y inner
close Y
continues
close X
caught 'k'
None

Process finished with exit code 0
