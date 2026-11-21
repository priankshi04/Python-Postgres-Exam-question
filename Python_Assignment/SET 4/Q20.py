from collections import Counter, deque, namedtuple, ChainMap, OrderedDict, defaultdict


c1 = Counter("abracadabra")
c2 = Counter(a=2, b=1, z=5)

print(c1.most_common(2), c1 - c2 == Counter("abracadabra") - c2)
print(sorted((c1 + c2).items()))
print(sorted((c1 & c2).items()), sorted((c1 | c2).items()))

c1.subtract(c2)

print(c1["z"], c1.total(), sorted((+c1).items()))


dq = deque(range(5), maxlen=4)

print(dq)

dq.rotate(1)

print(dq)

dq.appendleft("x")

print(dq)

dq.extend([7, 8])

print(dq, dq.popleft(), dq.pop())


Pt = namedtuple("Pt", "x y", defaults=[0])
p = Pt(1)

print(p, p._replace(y=5), p._asdict(), Pt._fields, p == (1, 0))


defaults = {"color": "red", "size": 1}
cm = ChainMap({"size": 9}, defaults)

cm["new"] = 1

print(dict(cm), cm.maps[0])
print(defaults, cm.parents.maps)


od = OrderedDict(a=1, b=2, c=3)
od.move_to_end("a")

print(
    list(od),
    od == OrderedDict(b=2, c=3, a=1),
    od == {"a": 1, "b": 2, "c": 3},
    OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1)
)


tree = defaultdict(lambda: defaultdict(list))

tree["x"]["y"].append(1)
tree["x"]["z"]

print({k: dict(v) for k, v in tree.items()}, len(tree["q"]), list(tree))

#OUTPUT
[('a', 5), ('b', 2)] True
[('a', 7), ('b', 3), ('c', 1), ('d', 1), ('r', 2), ('z', 5)]
[('a', 2), ('b', 1)] [('a', 5), ('b', 2), ('c', 1), ('d', 1), ('r', 2), ('z', 5)]
-5 3 [('a', 3), ('b', 1), ('c', 1), ('d', 1), ('r', 2)]
deque([1, 2, 3, 4], maxlen=4)
deque([4, 1, 2, 3], maxlen=4)
deque(['x', 4, 1, 2], maxlen=4)
deque([2, 7], maxlen=4) 1 8
Pt(x=1, y=0) Pt(x=1, y=5) {'x': 1, 'y': 0} ('x', 'y') True
{'color': 'red', 'size': 9, 'new': 1} {'size': 9, 'new': 1}
{'color': 'red', 'size': 1} [{'color': 'red', 'size': 1}]
['b', 'c', 'a'] True True False
{'x': {'y': [1], 'z': []}} 0 ['x', 'q']

Process finished with exit code 0
