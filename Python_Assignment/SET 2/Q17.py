class Guard:
    def __init__(self, name, suppress=(), fail_on_exit=False):
        self.name, self.suppress, self.fail = name, suppress, fail_on_exit

    def __enter__(self):
        print("enter", self.name)
        return self

    def __exit__(self, et, ev, tb):
        print("exit", self.name, et.__name__ if et else None)

        if self.fail:
            raise RuntimeError("exit-" + self.name)

        return et is not None and issubclass(et, self.suppress)


def f1():
    with Guard("a", (KeyError,)):
        with Guard("b"):
            raise KeyError("x")
        print("not here")

    return "f1 done"


def f2():
    try:
        with Guard("c", fail_on_exit=True):
            raise ValueError("body")
    except RuntimeError as e:
        print("caught", e, "| context:", repr(e.__context__))


def f3():
    with Guard("d", (ValueError,)) as g, Guard("e", fail_on_exit=True):
        return "f3 value"

    print("after")


print(f1())
f2()
print(f3())
#SOLUTION
enter a
enter b
exit b KeyError
exit a KeyError
f1 done
enter c
exit c ValueError
caught exit-c | context: ValueError('body')
enter d
enter e
exit e None
exit d RuntimeError
Traceback (most recent call last):
  File "C:\Users\Priankshi\PycharmProjects\Python_Assignment\SET 2\Q17.py", line 44, in <module>
    print(f3())
          ~~^^
  File "C:\Users\Priankshi\PycharmProjects\Python_Assignment\SET 2\Q17.py", line 36, in f3
    with Guard("d", (ValueError,)) as g, Guard("e", fail_on_exit=True):
                                         ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Priankshi\PycharmProjects\Python_Assignment\SET 2\Q17.py", line 13, in __exit__
    raise RuntimeError("exit-" + self.name)
RuntimeError: exit-e

Process finished with exit code 1