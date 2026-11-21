import json
from datetime import date


data = {
    1: "a",
    2.5: ("x", (1, 2)),
    None: True,
    False: 0,
    "s": {"k": None}
}

text = json.dumps(data)

print(text)

back = json.loads(text)

print(back)
print(back == data, back["1"], list(back))


class Enc(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return {"__date__": o.isoformat()}

        if isinstance(o, set):
            return sorted(o)

        return super().default(o)


def hook(d):
    if "__date__" in d:
        return date.fromisoformat(d["__date__"])

    return d


payload = {
    "when": date(2024, 2, 29),
    "tags": {"b", "a"},
    "n": (1, 2)
}

s = json.dumps(payload, cls=Enc, sort_keys=True, separators=(",", ":"))

print(s)

r = json.loads(s, object_hook=hook)

print(r)

try:
    json.dumps({"c": 1 + 2j}, cls=Enc)
except TypeError as e:
    print("TypeError:", e)

print(json.dumps({"x": float("nan")}), json.loads('{"a": NaN}'))

try:
    json.dumps({"x": float("nan")}, allow_nan=False)
except ValueError as e:
    print("ValueError:", e)
#SOLUTION
{"1": "a", "2.5": ["x", [1, 2]], "null": true, "false": 0, "s": {"k": null}}
{'1': 'a', '2.5': ['x', [1, 2]], 'null': True, 'false': 0, 's': {'k': None}}
False a ['1', '2.5', 'null', 'false', 's']
{"n":[1,2],"tags":["a","b"],"when":{"__date__":"2024-02-29"}}
{'n': [1, 2], 'tags': ['a', 'b'], 'when': datetime.date(2024, 2, 29)}
TypeError: Object of type complex is not JSON serializable
{"x": NaN} {'a': nan}
ValueError: Out of range float values are not JSON compliant: nan

Process finished with exit code 0
