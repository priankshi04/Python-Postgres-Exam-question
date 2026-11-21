import functools

def retry(times):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            attempts = 0
            while True:
                attempts += 1
                try:
                    return fn(*args, **kwargs)
                except ValueError as e:
                    print("fail", attempts, e)
                    if attempts >= times:
                        raise RuntimeError("gave up") from e

        return wrapper
    return deco


calls = {"n": 0}

@retry(3)
def flaky(x):
    calls["n"] += 1
    if calls["n"] < 3:
        raise ValueError(f"bad{calls['n']}")
    return x * 10


print(flaky(4), flaky.__name__)

calls["n"] = -10

try:
    flaky(1)
except RuntimeError as e:
    print(type(e.__cause__).__name__, e.__cause__, calls)
#SOLUTION
fail 1 bad1
fail 2 bad2
40 flaky
fail 1 bad-9
fail 2 bad-8
fail 3 bad-7
ValueError bad-7 {'n': -7}