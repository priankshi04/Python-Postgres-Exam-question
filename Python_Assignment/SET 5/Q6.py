import functools

depth = 0
log = []


def trace(fn):
    @functools.wraps(fn)
    def wrapper(*args):
        global depth

        log.append(" " * depth + f"{fn.__name__}{args}")
        depth += 1

        try:
            result = fn(*args)
            log.append(" " * depth + f"= {result}")
            return result
        finally:
            depth -= 1

    return wrapper


@trace
def fact(n):
    if n < 0:
        raise ValueError("negative")

    return 1 if n <= 1 else n * fact(n - 1)


@trace
def safe(n):
    try:
        return fact(n)
    except ValueError:
        return -1


print(safe(3))
print(safe(-2))
print(depth)
print("\n".join(log))

#OUTPUT
6
-1
0
safe(3,)
 fact(3,)
  fact(2,)
   fact(1,)
    = 1
   = 2
  = 6
 = 6
safe(-2,)
 fact(-2,)
 = -1

Process finished with exit code 0
