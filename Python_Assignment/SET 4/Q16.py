def gen():
    try:
        x = yield 1
        print("got", x)
        yield 2
    except ValueError:
        print("caught inside")
        yield "recovered"
    finally:
        print("gen cleanup")


g = gen()

print(next(g))
print(g.throw(ValueError))
print(next(g, "done"))


def bad():
    yield 1
    raise StopIteration("oops")


try:
    print(list(bad()))
except RuntimeError as e:
    print("RuntimeError:", e, type(e.__cause__).__name__)


def sub():
    yield "a"
    return 99


def collect():
    r = yield from sub()
    print("sub returned", r)


print(list(collect()))

it = iter(gen())

print(next(it))

try:
    it.throw(KeyError("k"))
except KeyError as e:
    print("KeyError escaped:", e)

print(next(it, "gone"))

OUTPUT
1
caught inside
recovered
gen cleanup
done
RuntimeError: generator raised StopIteration StopIteration
sub returned 99
['a']
1
gen cleanup
KeyError escaped: 'k'
gone

Process finished with exit code 0
