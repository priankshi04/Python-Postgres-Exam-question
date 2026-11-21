import sys
import unicodedata

a = "caf\u00e9"
b = "cafe\u0301"
nfc = lambda s: unicodedata.normalize("NFC", s)

print(a == b, len(a), len(b), nfc(a) == nfc(b))
print(a.encode("utf-8"), len(a.encode("latin-1")))

words = ["\u00e9clair", "zebra", "apple", "\u00e0 la carte"]

print(sorted(words) == sorted(words, key=lambda w: w.encode("utf-8")))
print(sorted(words, key=lambda w: unicodedata.normalize("NFD", w)))

try:
    b.encode("ascii")
except UnicodeEncodeError as e:
    print(e.start, e.reason)

print(b.encode("ascii", "replace"), b.encode("ascii", "backslashreplace"))
print(b"caf\xc3\xa9".decode("latin-1"), len(r"\u00e9"), len("\u00e9"))

x, y = "".join(["py", "thon"]), "python"
print(x == y, x is y, sys.intern(x) is y)

#OUTPUT
False 4 5 True
b'caf\xc3\xa9' 4
True
['apple', 'à la carte', 'éclair', 'zebra']
4 ordinal not in range(128)
b'cafe?' b'cafe\\u0301'
cafÃ© 6 1
True False True

Process finished with exit code 0