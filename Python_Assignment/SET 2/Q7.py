import functools


def traced(gen_fn):
    @functools.wraps(gen_fn)
    def wrapper(*a, **k):
        print("start", gen_fn.__name__)

        for item in gen_fn(*a, **k):
            print("item", item)
            yield item * 10

        print("end")

    return wrapper


@traced
def count(n):
    print("body")

    for i in range(1, n + 1):
        yield i


g = count(2)
print("created")
print(type(g).__name__)
print(next(g))
print(list(g))
print(count.__name__)


def noisy(fn):
    def w(*a, **k):
        print("calling")
        return fn(*a, **k)

    return w


@noisy
def gen():
    print("running")
    yield 1


x = gen()
print("got x")
print(next(x))
#SOLUTION
created
generator
start count
body
item 1
10
item 2
end
[20]
count
calling
got x
running
1

Process finished with exit code 0
