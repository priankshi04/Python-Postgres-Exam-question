nums = [1, 2, 3, 4]
m = map(lambda a, b: a * b, nums, [10, 20, 30])

print(next(m))
nums.append(5)
print(list(m))
print(list(m))

f = filter(None, [0, 1, "", "a", [], [0], None, 0.0])
print(list(f))

pairs = list(map(lambda x, y=2: x ** y, range(4)))
print(pairs)

adders = list(map(lambda n: lambda x: x + n, range(3)))
print([a(10) for a in adders])

z = list(zip(*map(lambda t: (t, t * t), range(1, 4))))
print(z)
#SOLUTION
10
[40, 90]
[]
[1, 'a', [0]]
[0, 1, 4, 9]
[10, 11, 12]
[(1, 2, 3), (1, 4, 9)]

Process finished with exit code 0
