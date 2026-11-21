class A:
    def __init__(self, **kw):
        print("A.init", kw)
        super().__init__(**kw)


class B(A):
    def __init__(self, b=0, **kw):
        print("B.init", b)
        super().__init__(**kw)


class C(A):
    def __init__(self, c=0, **kw):
        print("C.init", c)
        super().__init__(**kw)


class D(B, C):
    def __init__(self, d=0, **kw):
        print("D.init", d)
        super().__init__(**kw)


x = D(d=1, b=2, c=3)
print([k.__name__ for k in D.__mro__])

try:
    y = D(d=1, z=9)
except TypeError:
    print("TypeError")
#SOLUTION
D.init 1
B.init 2
C.init 3
A.init {}
['D', 'B', 'C', 'A', 'object']
D.init 1
B.init 0
C.init 0
A.init {'z': 9}
TypeError
