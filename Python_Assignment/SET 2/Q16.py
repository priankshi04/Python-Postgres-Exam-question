import itertools


class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1


class Repeater:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return iter(range(self.n, 0, -1))


c = Countdown(3)
r = Repeater(3)

print(list(c), list(c))
print(list(r), list(r))
print(list(zip(r, r)))

c = Countdown(3)
print(list(zip(c, c)))

c = Countdown(5)
print(list(itertools.islice(c, 2)), list(c))

it = iter(Countdown(4))
print(list(itertools.takewhile(lambda v: v > 2, it)), next(it))
#SOLUTION
[3, 2, 1] []
[3, 2, 1] [3, 2, 1]
[(3, 3), (2, 2), (1, 1)]
[(3, 2)]
[5, 4] [3, 2, 1]
[4, 3] 1

Process finished with exit code 0
