from dataclasses import dataclass, field, replace


@dataclass(order=True)
class Task:
    priority: int
    name: str = field(compare=False)
    tags: list = field(default_factory=list, compare=False)
    id: int = field(init=False, default=0, compare=False)

    _next = 0

    def __post_init__(self):
        Task._next += 1
        self.id = Task._next


a = Task(2, "write")
b = Task(1, "test", ["x"])
c = Task(2, "ship")

print(a < b, a == c, a is c, sorted([a, b, c])[0].name)
print(a)

c2 = replace(b, name="test2")
print(c2.tags is b.tags, c2.id, Task._next)

try:
    @dataclass
    class Bad:
        items: list = []
except ValueError as e:
    print("ValueError:", e)


@dataclass(frozen=True)
class P:
    x: int


p = P(1)

try:
    p.x = 5
except Exception as e:
    print(type(e).__name__)

print(hash(p) == hash(P(1)), {p: 1}[P(1)])
#SOLUTION
False True False test
Task(priority=2, name='write', tags=[], id=1)
True 4 4
ValueError: mutable default <class 'list'> for field items is not allowed: use default_factory
FrozenInstanceError
True 1

Process finished with exit code 0
