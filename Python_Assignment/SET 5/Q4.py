import functools


def limit(n):
    def deco(fn):
        state = {"count": 0}

        @functools.wraps(fn)
        def wrapper(*a, **k):
            if state["count"] >= n:
                raise RuntimeError(f"{fn.__name__} limit {n}")

            state["count"] += 1
            return fn(*a, **k)

        wrapper.remaining = lambda: n - state["count"]

        return wrapper

    return deco


shared = limit(2)


@shared
def a():
    return "a"


@shared
def b():
    return "b"


@limit(2)
def c():
    return "c"


print(a(), a())

try:
    a()
except RuntimeError as e:
    print(e)

print(b(), b.remaining(), a.remaining())

print(c(), c(), c.remaining())

try:
    c()
except RuntimeError as e:
    print(e)

print(a.remaining is b.remaining, a.__name__)

#OUTPUT
a a
a limit 2
b 1 0
c c 0
c limit 2
False a

Process finished with exit code 0