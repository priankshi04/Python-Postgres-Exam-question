first, *mid, last = "python"
a, (b, *c), *d = 1, "xyz", 3, 4

print(first, mid, last)
print(a, b, c, d)


def show(*args, **kw):
    return args, kw


d1, d2 = {"a": 1, "b": 2}, {"b": 3, "c": 4}

print(show(*"ab", *range(2), **d1))
print({**d1, **d2, "a": 0}, {"a": 0, **d1})

*p, q = {1: "a", 2: "b"}
print(p, q)

for thunk in (lambda: show(**d1, **d2),
              lambda: [x for x, *y in [[]]]):
    try:
        thunk()
    except (TypeError, ValueError) as e:
        print(type(e).__name__, e)
#SOLUTION
p ['y', 't', 'h', 'o'] n
1 x ['y', 'z'] [3, 4]
(('a', 'b', 0, 1), {'a': 1, 'b': 2})
{'a': 0, 'b': 3, 'c': 4} {'a': 1, 'b': 2}
[1] 2
TypeError __main__.show() got multiple values for keyword argument 'b'
ValueError not enough values to unpack (expected at least 1, got 0)

Process finished with exit code 0
