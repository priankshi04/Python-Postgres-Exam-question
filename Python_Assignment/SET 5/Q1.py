s = "a\tb\\n"

print(len(s), repr(s), s.split("\\"), r"a\tb".split("\\t"))

t = s
t += "!"

print(s == "a\tb\\n", t == s + "!", s is t)

print("a,b,,c".split(","), "a,b,,c".split(",", 1), " a b ".split(), " a b ".split(" "))

parts = "k1=v1;k2=;=v3;k4=a=b".split(";")

print(dict(map(lambda p: p.partition("=")[::2], parts)))

print("-".join("abc"), "ab".join(["1", "2", "3"]), "x".join([]) == "")

print("straße".upper(), "straße".casefold() == "STRASSE".casefold(),
      "straße".lower() == "straße")

print("10" < "9", sorted(["10", "9", "2"]), sorted(["10", "9", "2"], key=lambda v: int(v)),
      "Z" < "a")

table = str.maketrans({"a": "1", "b": None, "c": "xyz"})

print("abcabc".translate(table), "abc".translate(str.maketrans("ab", "ba")))

print("".join(filter(lambda ch: ch not in "aeiou", "education")))

#OUTPUT
5 'a\tb\\n' ['a\tb', 'n'] ['a', 'b']
True True False
['a', 'b', '', 'c'] ['a', 'b,,c'] ['a', 'b'] ['', 'a', 'b', '']
{'k1': 'v1', 'k2': '', '': 'v3', 'k4': 'a=b'}
a-b-c 1ab2ab3 True
STRASSE True True
True ['10', '2', '9'] ['2', '9', '10'] True
1xyz1xyz bac
dctn

Process finished with exit code 0