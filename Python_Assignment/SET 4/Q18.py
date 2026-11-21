import copy
import types


t = (1, [2, 3])
u = (1, 2)

print(copy.copy(t) is t, copy.deepcopy(t) is t, copy.deepcopy(u) is u)

t2 = copy.deepcopy(t)
t2[1].append(4)

print(t, t2)

f = lambda x: x

print(copy.copy(f) is f, copy.deepcopy(f) is f)

s = "text"

print(copy.deepcopy(s) is s, copy.copy([]) is [])

a = [1, 2]
b = a[:]
c = list(a)
d = a.copy()

print(a is b, b is c, c is d, a == b == c == d)

nested = {"k": [1]}
sh = nested.copy()
sh["k"].append(2)
sh["n"] = 0

print(nested, sh)

ns = types.SimpleNamespace(v=[1])
ns2 = copy.copy(ns)
ns2.v.append(2)
ns2.w = 1

print(ns, ns2)

OUTPUT
True False True
(1, [2, 3]) (1, [2, 3, 4])
True True
True False
False False False True
{'k': [1, 2]} {'k': [1, 2], 'n': 0}
namespace(v=[1, 2]) namespace(v=[1, 2], w=1)

Process finished with exit code 0