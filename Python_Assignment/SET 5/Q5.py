def double(fn):
    return lambda *a, **k: fn(*a, **k) * 2


def inc(fn):
    return lambda *a, **k: fn(*a, **k) + 1


def neg_args(fn):
    return lambda *a, **k: fn(*[-x for x in a], **{key: -v for key, v in k.items()})


@double
@inc
def f(x):
    return x


@inc
@double
def g(x):
    return x


@neg_args
@double
@inc
def h(x, y=0):
    return x + y


print(f(3), g(3), h(3), h(3, y=1), f.__name__)
print((lambda: None).__name__, f.__name__ == "<lambda>")

#OUTPUT
8 7 -4 -6 <lambda>
<lambda> True

Process finished with exit code 0
