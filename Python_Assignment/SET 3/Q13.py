class A:
    x = property(lambda self: "property")
    y = "class-attr"

    def m(self):
        return "method"


a = A()

a.__dict__["x"] = "inst-x"
a.__dict__["y"] = "inst-y"
a.__dict__["m"] = lambda: "inst-m"

print(a.x, a.y, a.m())
print(A.x.__class__.__name__, A.y, A.m.__class__.__name__)

try:
    a.x = "new"
except AttributeError:
    print("AttributeError")

del a.__dict__["m"]

print(a.m(), A.m(a))

b = A()
b.z = 1

print(sorted(vars(b)), hasattr(A, "z"))

A.z = 2

print(b.z, A().z)

del b.z

print(b.z)

OUTPUT
property inst-y inst-m
property class-attr function
AttributeError
method method
['z'] False
1 2
2

Process finished with exit code 0