def f(lst, d, n, s, t):
    lst.append(1)
    lst = lst + [2]
    d["k"] = d.get("k", 0) + 1
    d = {}
    n += 1
    s += "x"
    t += (1,)
    return lst, d, n, s, t


L, D, N, S, T = [0], {}, 5, "a", (0,)

r = f(L, D, N, S, T)

print(L, D, N, S, T)
print(r)
print(r[0] is L, r[1] is D, r[3] == S + "x")

a = b = []

a.append(1)
a = a + [2]

print(a, b, a is b)

x = [[0]] * 2
y = x[:]

y[0].append(1)
y[1] = ["new"]

print(x, y)


#OUTPUT
[0, 1] {'k': 1} 5 a (0,)
([0, 1, 2], {}, 6, 'ax', (0, 1))
False False True
[1, 2] [1] False
[[0, 1], [0, 1]] [[0, 1], ['new']]

Process finished with exit code 0