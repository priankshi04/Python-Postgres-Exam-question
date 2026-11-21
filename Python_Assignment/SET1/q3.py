from functools import reduce
compose = lambda *fs: lambda x: reduce(lambda acc, f: f(acc), fs, x)
steps = []
for k in range(1, 4):
    steps.append(lambda v: v * k)
p1 = compose(*steps, lambda v: v + 1)
p2 = compose(*[(lambda k: lambda v: v * k)(k) for k in range(1, 4)],
lambda v: v + 1)
print(p1(2), p2(2))
k = 10
print(p1(2), p2(2))
data = [1, 2, 3, 4, 5, 6]
threshold = 2
evens = filter(lambda v: v % 2 == 0, data)
big = (v for v in evens if v > threshold)
threshold = 4
data.append(8)
print(next(big))
data.append(10)
print(list(big))
print(list(evens))
#SOLUTION
55 13
2001 13
6
[8, 10]
[]
