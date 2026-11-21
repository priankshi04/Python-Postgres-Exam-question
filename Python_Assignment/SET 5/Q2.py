emps = [
    {"n": "ann", "d": "ops", "s": 50},
    {"n": "bob", "d": "dev", "s": 70},
    {"n": "cy", "d": "ops", "s": 50},
    {"n": "di", "d": "dev", "s": None},
    {"n": "ed", "d": "ops", "s": 65},
]

by = sorted(emps, key=lambda e: (e["d"], -(e["s"] or 0), e["n"]))

print([e["n"] for e in by])

k1 = lambda e: (e["s"] is None, e["s"] or 0)

print([e["n"] for e in sorted(emps, key=k1)])

step = sorted(emps, key=lambda e: e["n"], reverse=True)
step = sorted(step, key=lambda e: e["d"])

print([e["n"] for e in step])

print(max(emps, key=lambda e: e["s"] or 0)["n"],
      min(emps, key=lambda e: (e["s"] is None, e["s"]))["n"])

#OUTPUT
['bob', 'di', 'ed', 'ann', 'cy']
['ann', 'cy', 'ed', 'bob', 'di']
['di', 'bob', 'ed', 'cy', 'ann']
bob ann

Process finished with exit code 0