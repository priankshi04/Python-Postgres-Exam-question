rows = [("apple", 3, 1.5), ("kiwi", 12, 0.25), ("banana", 7, 10.0)]
w = 8
fmt = lambda name, qty, price: f"{name:<{w}}|{qty:>4d}|{price:>8.2f}|{qty * price:08.1f}"

for r in rows:
    print(fmt(*r))

print(f"{1234567.891:,.2f} {0.256:.1%} {255:#x} {255:08b} {'x':^5}|{'y':*>4}")

n = 42
print(f"{n=} {n!r:>6} {n:+d} {n:e}")

name = "Zo\u00eb"
print(f"{name!r} {name!a} {name:>6}|{len(name)}")

print("{0} {0!r} {1:{2}.{3}f}".format("a", 3.14159, 8, 3))

print(max(rows, key=lambda r: r[1] * r[2])[0], "%-6s|%5.1f|%x" % ("ab", 2.25, 255))

output
apple   |   3|    1.50|000004.5
kiwi    |  12|    0.25|000003.0
banana  |   7|   10.00|000070.0
1,234,567.89 25.6% 0xff 11111111   x  |***y
n=42     42 +42 4.200000e+01
'Zoë' 'Zo\xeb'    Zoë|3
a 'a'    3.142
banana ab    |  2.2|ff

Process finished with exit code 0