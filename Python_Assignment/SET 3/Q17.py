import functools


def primed(gen_fn):
    @functools.wraps(gen_fn)
    def wrapper(*a, **k):
        g = gen_fn(*a, **k)
        print("primed ->", next(g))
        return g
    return wrapper


@primed
def averager():
    total, n, avg = 0, 0, None

    try:
        while True:
            x = yield avg

            if x is None:
                continue

            total += x
            n += 1
            avg = total / n

    except ValueError as e:
        print("reset:", e)
        yield "reset-ack"

    finally:
        print("averager closed")


g = averager()

print(g.send(10))
print(g.send(20))
print(g.send(None))
print(g.throw(ValueError("manual")))
print(next(g, "exhausted"))
print(next(g, "exhausted"))

OUTPUT

primed -> None
10.0
15.0
15.0
reset: manual
reset-ack
averager closed
exhausted
exhausted

Process finished with exit code 0