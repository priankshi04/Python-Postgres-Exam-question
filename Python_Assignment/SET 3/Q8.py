class Report:
    def __init__(self, rows):
        self.rows = rows

    def render(self):
        return "\n".join([self.header(), *self.__lines(), self.footer()])

    def header(self):
        return "== report =="

    def footer(self):
        return f"-- {len(self.rows)} rows --"

    def __lines(self):
        return [self.fmt(r) for r in self.rows]

    def fmt(self, r):
        return str(r)


class CsvReport(Report):
    def header(self):
        return "a,b"

    def fmt(self, r):
        return ",".join(map(str, r))

    def __lines(self):
        return ["#" + self.fmt(r) for r in self.rows]

    def footer(self):
        return super().footer().upper()


r = CsvReport([(1, 2), (3, 4)])

print(r.render())
print(sorted(n for n in dir(r) if "lines" in n))
print(Report([5]).render() == Report.render(Report([5])))
print(type(r).__mro__[1].__name__, isinstance(r, Report), issubclass(Report, CsvReport))

OUTPUT
a,b
1,2
3,4
-- 2 ROWS --
['_CsvReport__lines', '_Report__lines']
True
Report True False

Process finished with exit code 0