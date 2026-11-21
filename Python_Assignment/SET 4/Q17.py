from contextlib import contextmanager, ExitStack, suppress


@contextmanager
def opened(name, fail_enter=False):
    print("open", name)

    if fail_enter:
        raise OSError(f"cannot open {name}")

    try:
        yield name
    finally:
        print("close", name)


def run(names):
    with ExitStack() as stack:
        stack.callback(print, "callback registered first")

        for n in names:
            stack.enter_context(opened(n, fail_enter=(n == "bad")))

        print("all open")
        return "ok"


print(run(["a", "b"]))

try:
    run(["a", "bad", "c"])
except OSError as e:
    print("OSError:", e)


with suppress(KeyError), opened("s"):
    raise KeyError("x")

print("after suppress")


@contextmanager
def twice():
    yield 1
    yield 2


try:
    with twice():
        pass
except RuntimeError as e:
    print("RuntimeError:", e)

OUTPUT
open a
open b
all open
close b
close a
callback registered first
ok
open a
open bad
close a
callback registered first
OSError: cannot open bad
open s
close s
after suppress
RuntimeError: generator didn't stop

Process finished with exit code 0