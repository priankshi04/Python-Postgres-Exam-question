class Bag:
    def __init__(self, *items):
        self.items = list(items)

    def __add__(self, other):
        print("add")
        return Bag(*self.items, *other.items)

    def __iadd__(self, other):
        print("iadd")
        self.items.extend(other.items)
        return self

    def __repr__(self):
        return f"Bag{tuple(self.items)}"


a = Bag(1)
b = a
c = Bag(2)

a += c
print(a, b, a is b)

a = a + c
print(a, b, a is b)


l1 = [1]
l2 = l1
l1 += [2]
l3 = l1
l1 = l1 + [3]

print(l1, l2, l3)


t1 = (1, 2)
t2 = t1
t1 += (3,)

print(t1, t2)


class NoIadd:
    def __init__(self, v):
        self.v = v

    def __add__(self, o):
        return NoIadd(self.v + o.v)

    def __repr__(self):
        return f"N{self.v}"


n1 = NoIadd(1)
n2 = n1
n1 += NoIadd(2)

print(n1, n2)


x = [1, 2]
y = (x, x)

try:
    y[0] += [3]
except TypeError as e:
    print("TypeError:", e)

print(y)

OUTPUT
iadd
Bag(1, 2) Bag(1, 2) True
add
Bag(1, 2, 2) Bag(1, 2) False
[1, 2, 3] [1, 2] [1, 2]
(1, 2, 3) (1, 2)
N3 N1
TypeError: 'tuple' object does not support item assignment
([1, 2, 3], [1, 2, 3])

Process finished with exit code 0