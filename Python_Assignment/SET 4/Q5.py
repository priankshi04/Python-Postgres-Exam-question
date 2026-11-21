import functools
import inspect


def plain(fn):
    def wrapper(*a, **k):
        """wrapper doc"""
        return fn(*a, **k)
    return wrapper


def wrapped(fn):
    @functools.wraps(fn)
    def wrapper(*a, **k):
        """wrapper doc"""
        return fn(*a, **k)

    wrapper.extra = True
    return wrapper


def base(x: int, y: str = "s") -> str:
    """base doc"""
    return y * x


base.version = 3

p, w = plain(base), wrapped(base)

print(p.__name__, p.__doc__, hasattr(p, "version"), hasattr(p, "__wrapped__"))
print(w.__name__, w.__doc__, w.version, w.__wrapped__ is base)
print(inspect.signature(p), inspect.signature(w))
print(w.__annotations__, p.__annotations__)

w.version = 4

print(base.version, w.version, w.extra, hasattr(base, "extra"))
print(wrapped(w).__wrapped__ is w, inspect.unwrap(wrapped(w)) is base)

OUTPUT
wrapper wrapper doc False False
base base doc 3 True
(*a, **k) (x: int, y: str = 's') -> str
{'x': <class 'int'>, 'y': <class 'str'>, 'return': <class 'str'>} {}
3 4 True False
True True

Process finished with exit code 0