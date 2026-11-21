import io
import json


class Item:
    def __init__(self, name, price):
        self.name, self.price = name, price

    def to_dict(self):
        return {"t": "Item", "name": self.name, "price": self.price}


class Order:
    def __init__(self, oid, items):
        self.oid, self.items = oid, items

    def to_dict(self):
        return {"t": "Order", "oid": self.oid, "items": self.items}

    def total(self):
        return sum(i.price for i in self.items)


class Enc(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, "to_dict"):
            return o.to_dict()
        return super().default(o)


REG = {
    "Item": lambda d: Item(d["name"], d["price"]),
    "Order": lambda d: Order(d["oid"], d["items"])
}


def hook(d):
    t = d.pop("t", None)
    return REG[t](d) if t else d


o = Order(7, [Item("pen", 1.5)])
buf = io.StringIO()

json.dump(
    {"order": o, "tags": ("a", "b")},
    buf,
    cls=Enc,
    sort_keys=True,
    separators=(",", ":")
)

print(buf.getvalue())

buf.seek(0)
back = json.load(buf, object_hook=hook)

print(type(back["order"]).__name__, [type(i).__name__ for i in back["order"].items], back["tags"])
print(back["order"].total(), back["order"].total() == o.total())
print(json.loads("[1, 2.0, 1e2, true, null]"))
print(json.dumps({"a": [1, {"b": None}]}, indent=1))

try:
    json.dumps({"o": o})
except TypeError as e:
    print("TypeError:", e)

OUTPUT
{"order":{"items":[{"name":"pen","price":1.5,"t":"Item"}],"oid":7,"t":"Order"},"tags":["a","b"]}
Order ['Item'] ['a', 'b']
1.5 True
[1, 2.0, 100.0, True, None]
{
 "a": [
  1,
  {
   "b": null
  }
 ]
}
TypeError: Object of type Order is not JSON serializable

Process finished with exit code 0