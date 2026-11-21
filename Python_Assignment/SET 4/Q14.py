def outer(*a, **k):
    def inner(*b, **c):
        return a, b, {**k, **c}
    return inner


f = outer(1, x=1)

print(f(2, y=2))
print(f(x=9))
print(outer()())


def merge(**kw):
    return kw


h = lambda **c: merge(**{"x": 1}, **c)

print(h(y=2))

try:
    h(x=5)
except TypeError as e:
    print("TypeError:", e)


def chain(*fs):
    def run(x, *args, **kwargs):
        for fn in fs:
            x = fn(x, *args, **kwargs)
        return x
    return run


add = lambda x, n=1: x + n
mul = lambda x, n=2, *, k=1: x * n * k


def show(thunk):
    try:
        print(thunk())
    except TypeError as e:
        print("TypeError:", e)


show(lambda: chain(add, mul)(3))
show(lambda: chain(add, mul)(3, 4))
show(lambda: chain(add, mul)(3, 4, k=10))
show(lambda: chain(add, mul)(3, 4, 5))

OUTPUT
((1,), (2,), {'x': 1, 'y': 2})
((1,), (), {'x': 9})
((), (), {})
{'x': 1, 'y': 2}
TypeError: __main__.merge() got multiple values for keyword argument 'x'
8
28
TypeError: <lambda>() got an unexpected keyword argument 'k'
TypeError: <lambda>() takes from 1 to 2 positional arguments but 3 were given

Process finished with exit code 0