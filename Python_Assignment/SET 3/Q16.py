import itertools


def readings():
    for k, v in [
        ("a", 1),
        ("a", 2),
        ("b", 5),
        ("a", 7),
        ("b", 1),
        ("b", 2)
    ]:
        print("read", k, v)
        yield k, v


groups = itertools.groupby(readings(), key=lambda t: t[0])

k1, g1 = next(groups)
print("first group", k1)

k2, g2 = next(groups)
print("second group", k2)

print(list(g1))
print(list(g2))

data = sorted([("a", 1), ("b", 5), ("a", 7)])

print([
    (k, sum(v for _, v in g))
    for k, g in itertools.groupby(data, key=lambda t: t[0])
])

OUTPUT
read a 1
first group a
read a 2
read b 5
second group b
[]
read a 7
[('b', 5)]
[('a', 8), ('b', 5)]

Process finished with exit code 0