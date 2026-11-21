import copy


class Doc:
    def __init__(self, title, meta, parts):
        self.title, self.meta, self.parts = title, meta, parts


meta = {"tags": ["a"]}

d1 = Doc("T", meta, [meta, meta])
d2 = copy.deepcopy(d1)

print(d2.parts[0] is d2.parts[1], d2.parts[0] is d2.meta, d2.meta is d1.meta)

d3 = copy.copy(d1)

d3.parts.append("x")
d3.title = "T3"

print(len(d1.parts), d1.title, d3.meta is d1.meta)

d2.meta["tags"].append("b")

print(d2.parts[1]["tags"], d1.meta["tags"])


class Tracked(Doc):
    def __deepcopy__(self, memo):
        print("deepcopy hook")
        return Tracked(
            self.title + "*",
            self.meta,
            copy.deepcopy(self.parts, memo)
        )


t = Tracked("T", meta, [meta])
t2 = copy.deepcopy(t)

print(t2.title, t2.meta is meta, t2.parts[0] is meta)

OUTPUT
True True False
3 T True
['a', 'b'] ['a']
deepcopy hook
T* True False

Process finished with exit code 0
