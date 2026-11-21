import itertools

log = []


def noisy(name, f):
    def g(x):
        log.append(f"{name}({x})")
        return f(x)
    return g


nums = itertools.count(1)
sq = map(noisy("sq", lambda x: x * x), nums)
odd = filter(noisy("odd", lambda x: x % 2), sq)

first = list(itertools.islice(odd, 3))

print(first, log)
print(next(nums), next(odd))
print(log[-3:])

lazy = (noisy("g", lambda x: x + 1)(v) for v in range(3))

print(len(log))
print(sum(lazy), len(log), sum(lazy))

OUTPUT
[1, 9, 25] ['sq(1)', 'odd(1)', 'sq(2)', 'odd(4)', 'sq(3)', 'odd(9)', 'sq(4)', 'odd(16)', 'sq(5)', 'odd(25)']
6 49
['odd(25)', 'sq(7)', 'odd(49)']
12
6 15 0

Process finished with exit code 0