def repeat(times=2):
    def deco(fn):
        def wrapper(*a, **k):
            return [fn(*a, **k) for _ in range(times)]
        return wrapper
    return deco


@repeat(3)
def hi():
    return "hi"


@repeat()
def yo():
    return "yo"


@repeat
def hey():
    return "hey"


print(hi(), yo())
print(hey.__name__, hey.__qualname__)
print(hey())

OUTPUT
['hi', 'hi', 'hi'] ['yo', 'yo']
deco repeat.<locals>.deco
Traceback (most recent call last):
  File "C:\Users\Priankshi\PycharmProjects\Python_Assignment\SET 3\Q5.py", line 26, in <module>
    print(hey())
          ~~~^^
TypeError: repeat.<locals>.deco() missing 1 required positional argument: 'fn'

Process finished with exit code 1
