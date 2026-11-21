def inner():
    got = yield 1
    print("inner got", got)

    try:
        yield 2
    finally:
        print("inner cleanup")

    return "done"


def outer():
    r = yield from inner()
    print("outer got", r)
    yield 3


g = outer()
print(next(g))
print(g.send("A"))
print(next(g))

g.close()

try:
    next(g)
except StopIteration:
    print("stopped")


g2 = outer()
print(next(g2))
print(g2.send(None))
g2.close()
print(g2.gi_frame is None)
#SOLUTION
1
inner got A
2
inner cleanup
outer got done
3
stopped
1
inner got None
2
inner cleanup
True

Process finished with exit code 0
