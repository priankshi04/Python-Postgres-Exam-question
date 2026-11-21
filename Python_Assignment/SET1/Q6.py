def timed(fn):
    print("decorating", fn.__name__)
    result = fn()

    def wrapper(*args, **kwargs):
        print("running", fn.__name__)
        return result

    return wrapper


@timed
def greet():
    print("hello")
    return "hi"


print(greet())
print(greet())


@timed
def add(a, b):
    return a + b


print(add(2, 3))
#SOLUTION
decorating greet
hello
running greet
hi
running greet
hi
decorating add