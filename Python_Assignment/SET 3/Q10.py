from abc import ABC, abstractmethod


class Discount(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply(self, price):
        ...

    def __call__(self, price):
        result = self.apply(price)
        assert result <= price, f"{self.name} raised the price"
        return round(result, 2)


class Percent(Discount):
    def __init__(self, pct):
        super().__init__(f"{pct}%")
        self.pct = pct

    def apply(self, price):
        return price * (1 - self.pct / 100)


class Flat(Discount):
    def __init__(self, amt):
        super().__init__(f"-{amt}")
        self.amt = amt

    def apply(self, price):
        return price - self.amt


class Surcharge(Flat):
    def apply(self, price):
        return price + self.amt


class Broken(Discount):
    pass


class Cart:
    def __init__(self, prices, *discounts):
        self.prices, self.discounts = prices, list(discounts)

    def total(self):
        t = sum(self.prices)
        for d in self.discounts:
            t = d(t)
        return t


cart = Cart([40, 60], Percent(10), Flat(5))

print(cart.total())

cart.discounts.reverse()
print(cart.total())

print(Cart([10], Flat(2.5), Percent(50)).total())

try:
    Cart([10], Surcharge(1)).total()
except AssertionError as e:
    print("AssertionError:", e)

try:
    Broken("x")
except TypeError:
    print("TypeError")

print(callable(Flat(1)), isinstance(Surcharge(1), Flat), Surcharge.__mro__[1].__name__)

OUTPUT
85.0
85.5
3.75
AssertionError: -1 raised the price
TypeError
True True Flat

Process finished with exit code 0