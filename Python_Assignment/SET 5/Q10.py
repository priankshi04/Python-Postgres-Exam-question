from functools import singledispatch, singledispatchmethod


class Shape:
    def area(self):
        return 0

    def area(self, scale):
        return 10 * scale


@singledispatch
def render(obj):
    return f"obj:{obj}"


@render.register
def _(obj: int):
    return f"int:{obj}"


@render.register(list)
def _(obj):
    return "list:" + ",".join(render(x) for x in obj)


@render.register(bool)
def _(obj):
    return f"bool:{obj}"


class Calc:
    @singledispatchmethod
    def add(self, a, b):
        return NotImplemented

    @add.register(int)
    def _(self, a, b):
        return a + b

    @add.register(str)
    def _(self, a, b):
        return a + str(b)


print(Shape().area(2))

try:
    Shape().area()
except TypeError:
    print("TypeError")

print(render(5), render(True), render(2.5), render(None))
print(render([1, [2, "x"], False]))
print(Calc().add(1, 2), Calc().add("a", 2), Calc().add(1.5, 2), Calc().add(True, 1))
print(sorted(c.__name__ for c in render.registry), render.dispatch(bool) is render.registry[bool])


#OUTPUT
20
TypeError
int:5 bool:True obj:2.5 obj:None
list:int:1,list:int:2,obj:x,bool:False
3 a2 NotImplemented 2
['bool', 'int', 'list', 'object'] True

Process finished with exit code 0