import copy


class Node:
    def __init__(self, v, kids=None):
        self.v = v
        self.kids = kids if kids is not None else []


shared = [1, 2]
a = Node("root", [Node("k1"), shared])

b = copy.copy(a)
c = copy.deepcopy(a)

b.v = "B"
b.kids.append("extra")
shared.append(3)
c.kids[1].append(99)

print(a.v, c.v, len(a.kids), len(c.kids))
print(b.kids is a.kids, c.kids[0] is a.kids[0], c.kids[1] is shared)
print(shared, c.kids[1])

a.kids.append(a)
d = copy.deepcopy(a)

print(d.kids[-1] is d, d.kids[-1] is a, len(d.kids))

e = copy.copy(a)
print(e.kids[-1] is a)
#SOLUTION
root root 3 2
True False False
[1, 2, 3] [1, 2, 99]
True False 4
True

Process finished with exit code 0
