import codecs
from string import ascii_letters

for l_ in ascii_letters + "ą":
    print(codecs.encode(l_, "utf-8"))

print(codecs.encode("123", "ascii"))
print(codecs.encode("QWERTY123", "ascii"))
codecs.encode("AĄ", "unicode")

x = 3
x_bytes = bytes(x)
len(x_bytes)
print(x)
print(x_bytes)

bytes("3", "utf-8")
