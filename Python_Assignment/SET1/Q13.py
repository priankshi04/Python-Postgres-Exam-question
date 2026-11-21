class Money:
    def __init__(self, amount, cur="USD"):
        self.amount, self.cur = amount, cur

    def __add__(self, other):
        if isinstance(other, Money) and other.cur == self.cur:
            return Money(self.amount + other.amount, self.cur)
        return NotImplemented

    def __radd__(self, other):
        return self if other == 0 else NotImplemented

    def __eq__(self, other):
        return (isinstance(other, Money)
                and (self.amount, self.cur) == (other.amount, other.cur))

    def __lt__(self, other):
        return self.amount < other.amount

    def __repr__(self):
        return f"Money({self.amount}, {self.cur!r})"


def show(thunk):
    try:
        print(thunk())
    except TypeError as e:
        print("TypeError:", e)


wallet = [Money(5), Money(3), Money(9)]

show(lambda: sum(wallet))
show(lambda: (sorted(wallet), max(wallet)))
show(lambda: (Money(5) == Money(5), Money(5) != Money(6), Money(5) == 5))
show(lambda: Money(5) in wallet)
show(lambda: {Money(5)})
show(lambda: Money(1) + 1)
show(lambda: Money(1) + Money(1, "EUR"))
show(lambda: 1 + Money(2))
show(lambda: Money(2) <= Money(2))
#SOLUTION
Money(17, 'USD')
([Money(3, 'USD'), Money(5, 'USD'), Money(9, 'USD')], Money(9, 'USD'))
(True, True, False)
True
TypeError: cannot use 'Money' as a set element (unhashable type: 'Money')
TypeError: unsupported operand type(s) for +: 'Money' and 'int'
TypeError: unsupported operand type(s) for +: 'Money' and 'Money'
TypeError: unsupported operand type(s) for +: 'int' and 'Money'
TypeError: '<=' not supported between instances of 'Money' and 'Money'

Process finished with exit code 0
