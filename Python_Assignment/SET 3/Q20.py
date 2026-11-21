import random


random.seed(2024)

first = [random.randrange(0, 10, 3) for _ in range(6)]

random.seed(2024)

second = [random.randrange(0, 10, 3) for _ in range(6)]

print(first == second, set(first) <= {0, 3, 6, 9})


random.seed(5)

deck = list(range(10))
orig = deck[:]

ret = random.shuffle(deck)

print(ret, sorted(deck) == orig)

random.seed(5)

deck2 = list(range(10))
random.shuffle(deck2)

print(deck == deck2)


random.seed(9)

s = random.sample(range(100), 5)

print(len(s) == len(set(s)), all(0 <= v < 100 for v in s))


state = random.getstate()

c1 = random.choices("abc", k=4)

random.setstate(state)

c2 = random.choices("abc", k=4)

print(c1 == c2, len(c1))


own = random.Random(1)
ref = random.Random(1)

random.seed(0)
random.random()

print([own.random() for _ in range(3)] == [ref.random() for _ in range(3)])


for thunk in (
    lambda: random.sample([1, 2], 3),
    lambda: random.choice([]),
    lambda: random.shuffle((1, 2, 3)),
    lambda: random.randint(5, 1)
):
    try:
        thunk()
    except Exception as e:
        print(type(e).__name__)

OUTPUT
True True
None True
True
True True
True 4
True
ValueError
IndexError
TypeError
ValueError

Process finished with exit code 0
