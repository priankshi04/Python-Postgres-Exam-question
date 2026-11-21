def make_once(f):
    return lambda *a, cache=[]: cache[0] if cache else cache.append(f(*a)) or cache[0]


calls = []


def expensive(tag):
    calls.append(tag)
    return tag.upper()


f1 = make_once(expensive)
f2 = make_once(expensive)

print(f1("a"), f1("b"), f2("c"), f1("z"), calls)
print(f1.__kwdefaults__, f2.__kwdefaults__)
print(f1("q", cache=[]), calls)

OUTPUT
A A C A ['a', 'c']
{'cache': ['A']} {'cache': ['C']}
Q ['a', 'c', 'q']

Process finished with exit code 0