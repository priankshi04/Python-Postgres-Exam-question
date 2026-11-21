registry = {}


def command(name=None, *, aliases=()):
    def deco(fn):
        for key in (name or fn.__name__, *aliases):
            if key in registry:
                print("duplicate", key)
            registry[key] = fn
        return fn
    return deco


@command()
def start():
    return "S"


@command("halt", aliases=("stop", "start"))
def stop():
    return "H"


@command(aliases=["x"])
def go():
    return "G"


print(sorted(registry))
print([registry[k]() for k in ("start", "halt", "stop", "x", "go")])
print(start(), start.__name__, registry["start"] is start)

#OUTPUT
duplicate start
['go', 'halt', 'start', 'stop', 'x']
['H', 'H', 'H', 'G', 'G']
S start False

Process finished with exit code 0