def stats(first, *rest, scale=1, **named):
    return first * scale, rest, named


args = (1, 2, 3)
kw = {"scale": 2, "tag": "t"}

print(stats(*args, **kw))
print(stats(*args[:1], *args[1:], scale=3))

head, *tail = stats(10, 20)

print(head, tail)

*init, last = [1, 2, 3, 4]

print(init, last)

a, b = {"x": 1, "y": 2}

print(a, b)

a, b = {"x": 1, "y": 2}.items()

print(a, b)

print(*[1, 2, 3], sep="-", end="!\n")

matrix = [[1, 2], [3, 4], [5, 6]]

print(list(zip(*matrix)), [*matrix[0], *matrix[2]])

print(max(*[3, 9, 2]), "%d-%d" % (*matrix[1],))

lam = lambda *a, **k: (len(a), sorted(k))

print(lam(*"ab", **{"z": 1, "y": 2}))

OUTPUT
C:\Users\Priankshi\PycharmProjects\Python_Assignment\.venv\Scripts\python.exe "C:\Users\Priankshi\PycharmProjects\Python_Assignment\SET 3\Q15.py"
(2, (2, 3), {'tag': 't'})
(3, (2, 3), {})
10 [(20,), {}]
[1, 2, 3] 4
x y
('x', 1) ('y', 2)
1-2-3!
[(1, 3, 5), (2, 4, 6)] [1, 2, 5, 6]
9 3-4
(2, ['y', 'z'])

Process finished with exit code 0