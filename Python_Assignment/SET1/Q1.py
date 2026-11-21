def build(n):
    return [lambda x: x + i for i in range(n)]
def build2(n):
    return [(lambda i: lambda x: x + i)(i) for i in range(n)]
a = build(3)
b = build2(3)
i = 100
print([f(10) for f in a])
print([f(10) for f in b])
print([f(10) for f in [lambda x, i=i: x + i for i in range(3)]])
#SOLUTION
[12, 12, 12]
[10, 11, 12]
[10, 11, 12]
