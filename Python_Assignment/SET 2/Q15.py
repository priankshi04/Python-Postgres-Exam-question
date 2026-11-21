def forward(fn):
    def w(*args, **kwargs):
        print("args", args[1:], "kwargs", kwargs)
        return fn(*args, **kwargs)

    return w


class Pt:
    def __init__(self, x, y, z=0):
        self.coords = (x, y, z)

    @forward
    def move(self, dx, dy, *rest, scale=1, **opts):
        self.coords = tuple(c + d * scale
                            for c, d in zip(self.coords, (dx, dy, *rest)))
        return opts


p = Pt(*[1, 2])

print(p.coords)
print(p.move(*(1, 1), 5, scale=2, **{"tag": "t"}))
print(p.coords)

opts = {"scale": 3}
p.move(1, 0, **opts, **{"note": 1})

print(p.coords)
#SOLUTION
(1, 2, 0)
args (1, 1, 5) kwargs {'scale': 2, 'tag': 't'}
{'tag': 't'}
(3, 4, 10)
args (1, 0) kwargs {'scale': 3, 'note': 1}
(6, 4)

Process finished with exit code 0
