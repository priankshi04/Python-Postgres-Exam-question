class Date:
    def __init__(self, y, m, d):
        self.y, self.m, self.d = y, m, d

    @classmethod
    def from_str(cls, s):
        y, m, d = map(int, s.split("-"))
        return cls(y, m, d)

    @classmethod
    def today(cls):
        return cls(2024, 1, 1)

    @staticmethod
    def is_leap(y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

    def next_year(self):
        return Date(self.y + 1, self.m, self.d)

    def next_year2(self):
        return type(self)(self.y + 1, self.m, self.d)

    def __repr__(self):
        return f"{type(self).__name__}({self.y}-{self.m}-{self.d})"


class Birthday(Date):
    def __init__(self, y, m, d, who="?"):
        super().__init__(y, m, d)
        self.who = who

    @classmethod
    def today(cls):
        return super().today()


print(Date.from_str("2024-02-29"), Birthday.from_str("2000-1-5"))
print(Birthday.today(), Date.today())

b = Birthday(2000, 1, 5, "amy")

print(b.next_year(), b.next_year2(), b.next_year2().who)
print(Date.is_leap(1900), b.is_leap(2000), Birthday.is_leap(2023))

OUTPUT
Date(2024-2-29) Birthday(2000-1-5)
Birthday(2024-1-1) Date(2024-1-1)
Date(2001-1-5) Birthday(2001-1-5) ?
False True False

Process finished with exit code 0
