class Account:
    def __init__(self, bal):
        self._bal = 0
        self.balance = bal

    @property
    def balance(self):
        return self._bal

    @balance.setter
    def balance(self, v):
        if v < 0:
            raise ValueError("negative")
        self._bal = v


class Savings(Account):
    @Account.balance.getter
    def balance(self):
        return round(self._bal * 1.1, 2)


class Locked(Account):
    @property
    def balance(self):
        return self._bal


a = Account(50)
s = Savings(100)

print(a.balance, s.balance)

s.balance = 200
print(s.balance, s._bal)

try:
    Locked(10)
except AttributeError:
    print("AttributeError")

try:
    a.balance = -1
except ValueError as e:
    print("ValueError", e)

print(Account.balance.fget is Savings.balance.fget,
      Savings.balance.fset is Account.balance.fset)
#SOLUTION
50 110.0
220.0 200
AttributeError
ValueError negative
False True

Process finished with exit code 0