import functools


def counted(fn):
    @functools.wraps(fn)
    def wrapper(*args):
        wrapper.calls += 1
        return fn(*args)

    wrapper.calls = 0
    return wrapper


def memo(fn):
    cache = {}

    @functools.wraps(fn)
    def wrapper(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return wrapper


@counted
@memo
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


@memo
@counted
def fib2(n):
    return n if n < 2 else fib2(n - 1) + fib2(n - 2)


print(fib(10), fib.calls)
print(fib2(10), fib2.calls)
print(fib2.__wrapped__.calls, fib2.__wrapped__ is fib2)
print(fib.__wrapped__.__name__, fib.__name__)
#SOLUTION
55 19
55 0
11 False
fib fib

Process finished with exit code 0
