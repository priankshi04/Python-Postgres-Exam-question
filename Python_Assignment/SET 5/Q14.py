def apply(fn, /, *args, times=1, **kw):
    return [fn(*args, **kw) for _ in range(times)]


def make_counter(start=0, step=1):
    n = start - step

    def counter():
        nonlocal n
        n += step
        return n

    return counter


c = make_counter(step=5)

print(apply(c, times=3), apply(c))
print(apply(sorted, [3, 1, 2], reverse=True), apply(max, 4, 9, key=lambda v: -v))
print(apply(print, "x", "y", sep="+", times=2))

for thunk in (lambda: apply(fn=c), lambda: apply(c, 3)):
    try:
        thunk()
    except TypeError as e:
        print("TypeError:", e)

gen = (i for i in range(3))

print(apply(lambda *a: a, *gen), apply(lambda *a: a, *gen))


#OUTPUT
[0, 5, 10] [15]
[[3, 2, 1]] [4]
x+y
x+y
[None, None]
TypeError: apply() missing 1 required positional argument: 'fn'
TypeError: make_counter.<locals>.counter() takes 0 positional arguments but 1 was given
[(0, 1, 2)] [()]

Process finished with exit code 0