def with_default(default_factory):
    def deco(fn):
        return lambda *a, **k: (
            lambda r: default_factory() if r is None else r
        )(fn(*a, **k))
    return deco


calls = []


@with_default(lambda: calls.append("factory") or [])
def find(xs, t):
    for x in xs:
        if x == t:
            return [x]


print(find([1, 2], 2), find([1, 2], 9), find.__name__, calls)

fs = []

for i in range(3):
    fs.append(with_default(lambda: i)(lambda x: None if x < 5 else x))

print([f(0) for f in fs], [f(7) for f in fs])

i = 10
print([f(0) for f in fs], [f(7) for f in fs])