class Counted:
    def __init__(self, fn):
        self.fn = fn
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.fn(*args, **kwargs)


@Counted
def square(x):
    return x * x


class Box:
    @Counted
    def area(self, w, h):
        return w * h


b = Box()
print(square(3), square(4), square.calls)

try:
    print(b.area(2, 3))
except TypeError as e:
    print("TypeError")

print(Box.area.calls)
print(Box.area(b, 2, 3))
print(Box.area.calls)
#SOLUTION
9 16 2
TypeError
1
6
2