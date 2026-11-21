import itertools
import random

rng = random.Random(3)
data = list("abcdef")
calls = []


def key(x):
    calls.append(x)
    return rng.random()


shuffled = sorted(data, key=key)

print(calls == data, sorted(shuffled) == data, len(calls))

rng.seed(3)

again = sorted(data, key=lambda _: rng.random())

print(again == shuffled)


def stream(seed):
    r = random.Random(seed)
    return (r.randint(1, 6) for _ in itertools.repeat(None))


a, b = stream(7), stream(7)

first = [next(a) for _ in range(5)]
second = [next(b) for _ in range(3)]

print(first[:3] == second, all(1 <= v <= 6 for v in first))

list(itertools.islice(b, 2))

print(next(a) == next(b))

random.seed(11)

g1 = (random.random() for _ in range(3))

x = next(g1)
y = random.random()

ref = random.Random(11)
r = [ref.random() for _ in range(3)]

print(x == r[0], y == r[1], next(g1) == r[2], len(list(g1)))

fs = [lambda: rng.random() for rng in (random.Random(1), random.Random(2))]

ref2 = random.Random(2)

print(fs[0]() == ref2.random(), fs[1]() == ref2.random())

#OUTPUT
True True 6
True
True True
True
True True True 1
True True

Process finished with exit code 0