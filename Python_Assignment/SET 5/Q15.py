def split(seq):
    head, *body, tail = seq
    return head, body, tail


print(split("abcd"), split([1, 2]), split(range(3)))

try:
    split([1])
except ValueError as e:
    print(e)

for a, *rest in [(1, 2, 3), (4,), (5, 6)]:
    print(a, rest)

nested = [(1, (2, 3)), (4, (5, 6))]

print([a + b + c for a, (b, c) in nested])


def gen():
    yield *[1, 2], 3


print(list(gen()))

x = [*range(3), *"ab", *{"k": 1}, *(9,)]

print(x, len({*x}), {**{"a": 1}, **{"a": 2, "b": 3}})


def f(a, b, *, c):
    return a + b + c


args = {"a": 1, "b": 2}

print(f(**args, c=3), f(*[1, 2], **{"c": 3}))

#OUTPUT
('a', ['b', 'c'], 'd') (1, [], 2) (0, [1], 2)
not enough values to unpack (expected at least 2, got 1)
1 [2, 3]
4 []
5 [6]
[6, 15]
[(1, 2, 3)]
[0, 1, 2, 'a', 'b', 'k', 9] 7 {'a': 2, 'b': 3}
6 6

Process finished with exit code 0