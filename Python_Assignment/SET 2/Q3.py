def make():
    n = 0
    bad = lambda: (n := n + 1)
    box = [0]
    good = lambda: box.__setitem__(0, box[0] + 1) or box[0]

    def nl():
        nonlocal n
        n += 1
        return n

    return bad, good, nl, lambda: n


bad, good, nl, peek = make()

print(good(), good(), nl(), nl(), peek())

try:
    bad()
except UnboundLocalError:
    print("UnboundLocalError")


curry = lambda f: lambda a: lambda b: lambda c: f(a, b, c)

add3 = curry(lambda x, y, z: x * 100 + y * 10 + z)

print(add3(1)(2)(3))

part = add3(4)
print(part(5)(6), part(7)(8))

fs = [curry(lambda x, y, z, k=k: x + y + z + k)(1)(2)
      for k in range(3)]

print([f(3) for f in fs])
#SOLUTION
1 2 1 2 2
UnboundLocalError
123
456 478
[6, 7, 8]

