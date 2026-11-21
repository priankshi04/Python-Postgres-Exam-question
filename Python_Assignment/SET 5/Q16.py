import itertools as it


print(list(it.product("ab", [1, 2])))

print(list(it.permutations("abc", 2))[:4], len(list(it.permutations(range(4)))))

print(list(it.combinations("abcd", 3)))

print(list(it.combinations_with_replacement("ab", 2)))

print(
    list(it.islice(it.cycle("xy"), 5)),
    list(it.repeat(7, 3)),
    list(map(pow, [2, 3], it.repeat(2)))
)

print(
    list(it.dropwhile(lambda v: v < 3, [1, 4, 2, 5, 1])),
    list(it.chain.from_iterable([[1], [], [2, 3]]))
)

a, b = it.tee(iter(range(3)))

print(next(a), next(a), list(b), list(a))

it1 = iter(range(5))

print(list(it.takewhile(lambda v: v < 2, it1)), list(it1))

print(
    list(it.starmap(lambda x, y: x * y, [(1, 2), (3, 4)])),
    list(it.zip_longest("ab", [1], fillvalue=0))
)

print(
    sum(1 for _ in it.product(range(3), repeat=3)),
    list(it.accumulate([1, 2, 3], initial=10))
)


#OUTPUT
[('a', 1), ('a', 2), ('b', 1), ('b', 2)]
[('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c')] 24
[('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]
[('a', 'a'), ('a', 'b'), ('b', 'b')]
['x', 'y', 'x', 'y', 'x'] [7, 7, 7] [4, 9]
[4, 2, 5, 1] [1, 2, 3]
0 1 [0, 1, 2] [2]
[0, 1] [3, 4]
[2, 12] [('a', 1), ('b', 0)]
27 [10, 11, 13, 16]

Process finished with exit code 0