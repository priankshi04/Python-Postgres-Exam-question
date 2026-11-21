class Grid:
    def __init__(self, rows, cols, fill=0):
        self.rows, self.cols = rows, cols
        self.cells = [fill] * (rows * cols)

    def _idx(self, key):
        r, c = key

        if not (0 <= r < self.rows and 0 <= c < self.cols):
            raise IndexError(f"({r}, {c}) out of range")

        return r * self.cols + c

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return self.cells[self._idx(key)]

        if isinstance(key, slice):
            return self.cells[key]

        return self.cells[key * self.cols:(key + 1) * self.cols]

    def __setitem__(self, key, value):
        self.cells[self._idx(key)] = value

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        for r in range(self.rows):
            yield self[r]

    def __contains__(self, v):
        return v in self.cells


g = Grid(2, 3)

g[0, 1] = 5
g[1, 2] = 7

print(g[0, 1], g[1], g[2:5], g[-1])
print(len(g), list(g), 7 in g, 8 in g)

try:
    g[2, 0]
except IndexError as e:
    print("IndexError:", e)

try:
    g[1, -1] = 1
except IndexError as e:
    print("IndexError:", e)

print([row for row in g if any(row)], bool(g))


#OUTPUT
5 [0, 0, 7] [0, 0, 0] []
6 [[0, 5, 0], [0, 0, 7]] True False
IndexError: (2, 0) out of range
IndexError: (1, -1) out of range
[[0, 5, 0], [0, 0, 7]] True

Process finished with exit code 0