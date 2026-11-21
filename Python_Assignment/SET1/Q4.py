def tag(name):
    print("make", name)
    def deco(fn):
        print("decorate", name, fn.__name__)
        def wrapper(*a, **k):
            print("enter", name)
            r = fn(*a, **k)
            print("exit", name)
            return r + 1
        return wrapper
    return deco
@tag("A")
@tag("B")
def f(x):
    print("f", x)
    return x * 2
print("defined")
print(f(5))
print(f.__name__)
#SOLUTION
make A
make B
decorate B f
decorate A wrapper
defined
enter A
enter B
f 5
exit B
exit A
12
wrapper