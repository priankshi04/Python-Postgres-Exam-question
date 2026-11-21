class Vault:
    def __init__(self, secret):
        self.__secret = secret
        self._hint = "see docs"
        self.public = 1

    def reveal(self):
        return self.__secret


v = Vault(42)

print(v.reveal(), v._hint)

try:
    v.__secret
except AttributeError:
    print("AttributeError")

print(v._Vault__secret)

v.__secret = "hacked"

print(v.reveal(), v.__secret, sorted(vars(v)))

v._Vault__secret = 0

print(v.reveal())
print(hasattr(v, "__secret"), getattr(v, "_Vault__secret"))


class Sub(Vault):
    def peek(self):
        return self.__secret


try:
    Sub(7).peek()
except AttributeError as e:
    print("AttributeError:", e)

print(Sub(7).reveal())


#OUTPUT
42 see docs
AttributeError
42
42 hacked ['_Vault__secret', '__secret', '_hint', 'public']
0
True 0
AttributeError: 'Sub' object has no attribute '_Sub__secret'
7

Process finished with exit code 0