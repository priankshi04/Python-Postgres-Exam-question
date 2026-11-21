def f(a, b=2, /, c=3, *args, d, e=5, **kw):
    return (a, b, c, args, d, e, kw)


calls = [
    "f(1, d=4)",
    "f(1, 2, 3, 4, 5, d=6, z=7)",
    "f(1, b=9, d=1)",
    "f(1, 2, 3, d=1, c=5)",
    "f(1)",
    "f(a=1, d=2)",
    "f(*[1, 2], **{'c': 7, 'd': 8})",
    "f(1, 2, 3, 4, d=5, **{'a': 'x'})",
]

for src in calls:
    try:
        print(src, "->", eval(src))
    except TypeError as e:
        print(src, "-> TypeError:", e)
#SOLUTION
f(1, d=4) -> (1, 2, 3, (), 4, 5, {})
f(1, 2, 3, 4, 5, d=6, z=7) -> (1, 2, 3, (4, 5), 6, 5, {'z': 7})
f(1, b=9, d=1) -> (1, 2, 3, (), 1, 5, {'b': 9})
f(1, 2, 3, d=1, c=5) -> TypeError: f() got multiple values for argument 'c'
f(1) -> TypeError: f() missing 1 required keyword-only argument: 'd'
f(a=1, d=2) -> TypeError: f() missing 1 required positional argument: 'a'
f(*[1, 2], **{'c': 7, 'd': 8}) -> (1, 2, 7, (), 8, 5, {})
f(1, 2, 3, 4, d=5, **{'a': 'x'}) -> (1, 2, 3, (4,), 5, 5, {'a': 'x'})

Process finished with exit code 0
