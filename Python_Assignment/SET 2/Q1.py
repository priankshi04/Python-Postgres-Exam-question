from collections import defaultdict

words = ["Banana", "apple", "cherry", "Apple", "banana", "Cherry", "date"]

print(sorted(words))
print(sorted(words, key=str.lower))
print(sorted(words, key=lambda w: (w.casefold(), w.islower())))

groups = defaultdict(list)
for w in words:
    groups[w[0].lower()].append(w)

by_size = sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0]))

print([(k, len(v)) for k, v in by_size])
print(max(words, key=lambda w: (len(w), w)))
print(list(map(lambda kv: kv[1][-1], sorted(groups.items()))))
print(groups["z"], "z" in groups, len(groups))
#SOLUTION
['Apple', 'Banana', 'Cherry', 'apple', 'banana', 'cherry', 'date']
['apple', 'Apple', 'Banana', 'banana', 'cherry', 'Cherry', 'date']
['Apple', 'apple', 'Banana', 'banana', 'Cherry', 'cherry', 'date']
[('a', 2), ('b', 2), ('c', 2), ('d', 1)]
cherry
['Apple', 'banana', 'Cherry', 'date']
[] True 5

Process finished with exit code 0
