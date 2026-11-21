class Pt:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, o):
        return isinstance(o, Pt) and (self.x, self.y) == (o.x, o.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Pt({self.x},{self.y})"


class Pt2(Pt):
    def __eq__(self, o):
        return isinstance(o, Pt) and self.x == o.x


p = Pt(1, 2)
d = {p: "first"}
s = {p}

print(d[Pt(1, 2)], Pt(1, 2) in s, p is Pt(1, 2))

p.x = 5

print(
    d.get(Pt(5, 2)),
    Pt(1, 2) in s,
    Pt(5, 2) in s,
    list(d) == [Pt(5, 2)],
    p in d
)

q = Pt2(1, 9)

print(q == Pt(1, 2), Pt(1, 2) == q)

try:
    hash(q)
except TypeError as e:
    print(e)

print(Pt2.__hash__ is None)

OUTPUT
first True False
None False False True False
True True
unhashable type: 'Pt2'
True
Traceback (most recent call last):
  File "C:\Users\Priankshi\PycharmProjects\Python_Assignment\SET 3\Q11.py", line 47, in <module>
    OUTPUT
NameError: name 'OUTPUT' is not defined

Process finished with exit code 1
