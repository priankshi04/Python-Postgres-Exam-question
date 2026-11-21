import copy
from collections import defaultdict


grid = [[0] * 3] * 2
grid[0][1] = 7

print(grid)

grid2 = [[0] * 3 for _ in range(2)]
grid2[0][1] = 7

print(grid2)

d = dict.fromkeys(["a", "b"], [])
d["a"].append(1)

print(d)

reg = defaultdict(list)
reg["x"].append(1)

snap = dict(reg)
snap2 = copy.deepcopy(reg)

reg["x"].append(2)
reg["y"].append(3)

print(snap, snap2, dict(reg))
print(type(snap2).__name__, snap2.default_factory is list)
#SOLUTION
[[0, 7, 0], [0, 7, 0]]
[[0, 7, 0], [0, 0, 0]]
{'a': [1], 'b': [1]}
{'x': [1, 2]} defaultdict(<class 'list'>, {'x': [1]}) {'x': [1, 2], 'y': [3]}
defaultdict True

Process finished with exit code 0