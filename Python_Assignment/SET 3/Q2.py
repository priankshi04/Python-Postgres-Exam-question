from functools import reduce, partial
from itertools import accumulate

nums = [3, 1, 4, 1, 5]

print(list(accumulate(nums, lambda a, b: a * 10 + b)))
print(list(accumulate(nums, max, initial=2)))
print(reduce(lambda a, b: b + a, "abc"))
print(reduce(lambda acc, x: acc + [acc[-1] + x], nums, [0]))

mul = lambda a, b, c=1: a * b * c
dbl = partial(mul, 2)

print(dbl(5), dbl(5, 3), partial(mul, c=4)(2, 3))
print(list(map(lambda f: f(3), [dbl, partial(mul, 3, 3), lambda x: x ** 2])))
print(reduce(lambda a, b: a + b, [], "empty"))

try:
    reduce(lambda a, b: a + b, [])
except TypeError as e:
    print(e)

    #OUTPUT
[3, 31, 314, 3141, 31415]
[2, 3, 3, 4, 4, 5]
cba
[0, 3, 4, 8, 9, 14]
10 30 24
[6, 27, 9]
empty
reduce() of empty iterable with no initial value

Process finished with exit code 0
