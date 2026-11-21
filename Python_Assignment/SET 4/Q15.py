class Base:
    def __init__(self, *args, **kwargs):
        print("Base", args, kwargs)
        self.__dict__.update(kwargs)


class Mixin:
    def __init__(self, *args, tag="m", **kwargs):
        print("Mixin", tag)
        super().__init__(*args, **kwargs)
        self.tag = tag


class Widget(Mixin, Base):
    def __init__(self, name, *args, **kwargs):
        print("Widget", name)
        super().__init__(*args, **kwargs)
        self.name = name


w = Widget("w1", 1, 2, color="red", tag="T")

print(w.__dict__)

w2 = Widget(*["w2", "a"], **{"size": 3})

print(sorted(w2.__dict__.items()))
print(Widget.__mro__[1].__name__)

OUTPUT
Widget w1
Mixin T
Base (1, 2) {'color': 'red'}
{'color': 'red', 'tag': 'T', 'name': 'w1'}
Widget w2
Mixin m
Base ('a',) {'size': 3}
[('name', 'w2'), ('size', 3), ('tag', 'm')]
Mixin

Process finished with exit code 0