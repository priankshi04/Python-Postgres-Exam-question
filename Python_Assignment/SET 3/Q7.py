def loud(fn):
    def w(*a, **k):
        print("call", a[-1])
        return fn(*a, **k)
    return w


class C:
    @classmethod
    @loud
    def good(cls, x):
        return (cls.__name__, x)

    @loud
    @classmethod
    def bad(cls, x):
        return (cls.__name__, x)

    @loud
    @staticmethod
    def stat(x):
        return x * 2

    @staticmethod
    @loud
    def stat2(x):
        return x * 3


def attempt(thunk):
    try:
        print(thunk())
    except TypeError as e:
        print("TypeError:", e)


c = C()

attempt(lambda: C.good(1))
attempt(lambda: c.good(2))
attempt(lambda: C.bad(3))
attempt(lambda: c.bad(4))
attempt(lambda: C.stat(5))
attempt(lambda: c.stat(6))
attempt(lambda: C.stat2(7))

OUTPUT
call 1
('C', 1)
call 2
('C', 2)
call 3
TypeError: 'classmethod' object is not callable
call 4
TypeError: 'classmethod' object is not callable
call 5
10
call 6
TypeError: C.stat() takes 1 positional argument but 2 were given
call 7
21

Process finished with exit code 0
