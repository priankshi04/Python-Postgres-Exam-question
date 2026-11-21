class Temp:
    def __init__(self, c):
        self.celsius = c

    @property
    def celsius(self):
        return self.__c

    @celsius.setter
    def celsius(self, v):
        if v < -273.15:
            raise ValueError("below absolute zero")
        self.__c = v


class Lab(Temp):
    def reset(self):
        self.__c = 0
        return self.celsius


t = Lab(25)
print(t.reset())
print(t.__dict__)

t.celsius = -5
print(t.__dict__)

print(hasattr(t, "_Lab__c"), hasattr(t, "__c"))

try:
    Temp(-300)
except ValueError as e:
    print("ValueError:", e)

try:
    del t.celsius
except AttributeError:
    print("AttributeError")

t.fahrenheit = t.celsius * 9 / 5 + 32
print(sorted(vars(t)), t.fahrenheit)
#SOLUTION
25
{'_Temp__c': 25, '_Lab__c': 0}
{'_Temp__c': -5, '_Lab__c': 0}
True False
ValueError: below absolute zero
AttributeError
['_Lab__c', '_Temp__c', 'fahrenheit'] 23.0

Process finished with exit code 0