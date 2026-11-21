import itertools


def add_item(item, bucket=[], *, limit=3):
    if len(bucket) < limit:
        bucket.append(item)
    return bucket


a = add_item(1)
b = add_item(2)
c = add_item(3, [])
d = add_item(4, limit=2)
e = add_item(5)

print(a, b, c, d, e)
print(a is b, a is d, add_item.__defaults__)
print(add_item.__kwdefaults__)

tick = itertools.count(1)


def labeled(x, n=next(tick)):
    return (x, n)


print(labeled("a"), labeled("b"), next(tick))
#SOLUTION
[1, 2, 5] [1, 2, 5] [3] [1, 2, 5] [1, 2, 5]
True True ([1, 2, 5],)
{'limit': 3}
('a', 1) ('b', 1) 2

Process finished with exit code 0
