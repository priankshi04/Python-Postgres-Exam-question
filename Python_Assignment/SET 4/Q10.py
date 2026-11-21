class A:
    def who(self):
        return ["A"]


class B(A):
    def who(self):
        return ["B"] + super().who()


class C(A):
    def who(self):
        return ["C"] + super().who()


class D(B, C):
    def who(self):
        return ["D"] + super().who()


class E(C, B):
    pass


d = D()

print(d.who())
print(E().who())
print(super(B, d).who())
print(B.who(E()), C.who(d))
print([k.__name__ for k in D.mro()], [k.__name__ for k in E.__mro__])

try:
    class F(D, E):
        pass
except TypeError as e:
    print("TypeError")

OUTPUT
['D', 'B', 'C', 'A']
['C', 'B', 'A']
['C', 'A']
['B', 'A'] ['C', 'A']
['D', 'B', 'C', 'A', 'object'] ['E', 'C', 'B', 'A', 'object']
TypeError

Process finished with exit code 0