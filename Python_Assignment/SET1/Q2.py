from functools import reduce
records = [("amy", [3, 9, 4]), ("bob", [7, 7]),
           ("cal", [9, 1, 1, 1]), ("dee", [5, 5, 5])]
ranked = sorted(records, key=lambda t: (-max(t[1]), len(t[1]), t[0]))
print([n for n, _ in ranked])
print(reduce(lambda acc, t: acc + sum(t[1]) if len(t[1]) % 2 == 0 else acc * 2,
        records, 1))
print(max(records, key=lambda t: sum(t[1]) / len(t[1]))[0])
print(sorted(records, key=lambda t: len(t[1]), reverse=True)[0][0],
sorted(["bb", "a", "cc", "d"], key=len, reverse=True))
#SOLUTION
['amy', 'cal', 'bob', 'dee']
56
bob
cal ['bb', 'cc', 'a', 'd']
