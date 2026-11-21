import functools
import inspect
from idlelib.outwin import OutputWindow


class AppError(Exception):
    def __init__(self, msg, code=500):
        super().__init__(msg)
        self.code = code


def guard(*exc_types, code):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                print("enter", fn.__name__)
                return fn(*args, **kwargs)
            except exc_types as e:
                raise AppError(f"{fn.__name__} failed", code) from e
            finally:
                print("leave", fn.__name__)
        return wrapper
    return deco


@guard(KeyError, code=404)
@guard(ValueError, TypeError, code=400)
def load(d, k):
    return int(d[k])


for args in [
    ({"a": "5"}, "a"),
    ({"a": "x"}, "a"),
    ({}, "a"),
    ({"a": None}, "a")
]:
    try:
        print("result", load(*args))
    except AppError as e:
        print(
            "AppError",
            e,
            e.code,
            type(e.__cause__).__name__,
            type(e.__cause__.__cause__).__name__
        )
    except Exception as e:
        print(type(e).__name__)

print(load.__name__, inspect.signature(load), load.__wrapped__.__name__)

Output
enter load
enter load
leave load
leave load
result 5
enter load
enter load
leave load
leave load
AppError load failed 400 ValueError NoneType
enter load
enter load
leave load
leave load
AppError load failed 404 KeyError NoneType
enter load
enter load
leave load
leave load
AppError load failed 400 TypeError NoneType
load (d, k) load

Process finished with exit code 0