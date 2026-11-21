def shout(fn):
    def wrapper(text):
        return fn(text).upper() + "!"
    return wrapper


@shout
def greet(name, punct="."):
    """Greeting function."""
    return "hello " + name + punct


print(greet("bob"))
print(greet("amy", punct="?"))
print(greet.__name__, greet.__doc__)
#SOLUTION
HELLO BOB.!
Traceback (most recent call last):
  File "C:\Users\Priankshi\PycharmProjects\Python_Assignment\SET 2\Q5.py", line 14, in <module>
    print(greet("amy", punct="?"))
          ~~~~~^^^^^^^^^^^^^^^^^^
TypeError: shout.<locals>.wrapper() got an unexpected keyword argument 'punct'
