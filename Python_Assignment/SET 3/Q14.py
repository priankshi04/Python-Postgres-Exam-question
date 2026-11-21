import inspect


def f(a, /, b, c=3, *args, d, e=5, **kw):
    pass


sig = inspect.signature(f)

print(sig)

for p in sig.parameters.values():
    print(p.name, p.kind.name, p.default is inspect.Parameter.empty)

bound = sig.bind(1, 2, d=4, z=9)
bound.apply_defaults()

print(bound.arguments)

for call in (
    lambda: sig.bind(1),
    lambda: sig.bind(1, 2, 3, 4, 5, d=0),
    lambda: sig.bind(a=1, b=2, d=3),
    lambda: sig.bind_partial(1, d=2).arguments
):
    try:
        print(call())
    except TypeError as e:
        print("TypeError:", e)


OUTPUT
(a, /, b, c=3, *args, d, e=5, **kw)
a POSITIONAL_ONLY True
b POSITIONAL_OR_KEYWORD True
c POSITIONAL_OR_KEYWORD False
args VAR_POSITIONAL True
d KEYWORD_ONLY True
e KEYWORD_ONLY False
kw VAR_KEYWORD True
{'a': 1, 'b': 2, 'c': 3, 'args': (), 'd': 4, 'e': 5, 'kw': {'z': 9}}
TypeError: missing a required argument: 'b'
<BoundArguments (a=1, b=2, c=3, args=(4, 5), d=0)>
TypeError: missing a required positional-only argument: 'a'
{'a': 1, 'd': 2}

Process finished with exit code 0