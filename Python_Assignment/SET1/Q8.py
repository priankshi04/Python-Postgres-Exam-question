class Reg:
    count = 0
    items = []

    def __init__(self, name):
        self.name = name
        self.count += 1
        self.items.append(name)


a = Reg("a")
b = Reg("b")

print(a.count, b.count, Reg.count)

Reg.count = 10
print(a.count, b.count, Reg.count)

del a.count
print(a.count)

print(Reg.items is a.items, a.items)

a.items = a.items + ["z"]
print(a.items, b.items, Reg.items)
#SOLUTION
1 1 0
1 1 10
10
True ['a', 'b']
['a', 'b', 'z'] ['a', 'b'] ['a', 'b']
