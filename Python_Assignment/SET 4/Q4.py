import functools

calls = []


@functools.lru_cache(maxsize=2)
def f(x, y=0):
    calls.append((x, y))
    return x + y


f(1)
f(2)
f(1)

print(calls, f.cache_info())

f(3)
f(2)

print(calls, f.cache_info())

f(1, 0)
f(1, y=0)

print(calls[-3:], f.cache_info())

try:
    f([1])
except TypeError as e:
    print("TypeError:", e)

f.cache_clear()

print(f.cache_info(), f.__wrapped__(5), f.__name__)


class K:
    def __init__(self, v):
        self.v = v

    @functools.lru_cache(maxsize=None)
    def get(self, n):
        return self.v + n


a, b = K(1), K(10)

print(a.get(1), a.get(1), b.get(1), K.get.cache_info().hits, K.get.cache_info().misses)

OUTPUT
[(1, 0), (2, 0)] CacheInfo(hits=1, misses=2, maxsize=2, currsize=2)
[(1, 0), (2, 0), (3, 0), (2, 0)] CacheInfo(hits=1, misses=4, maxsize=2, currsize=2)
[(2, 0), (1, 0), (1, 0)] CacheInfo(hits=1, misses=6, maxsize=2, currsize=2)
TypeError: unhashable type: 'list'
CacheInfo(hits=0, misses=0, maxsize=2, currsize=0) 5 f
2 2 11 1 2

Process finished with exit code 0