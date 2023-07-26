
# lists
list_ = [1, 3, "a", "q", 222.23]
print(list_.pop())
print(list_)
print(list_.pop(1))
print(list_)
try:
    list_[22]
except IndexError:
    print(f"Caught {IndexError.__name__}")

# dictionaries
dict_ = {0: "qwerty", 1: "zxcv"}
dict_.update({2: "uyt"})
print(dict_)
another_dict = dict.fromkeys([0, 1, 2, 3,], "qwerty")
print(another_dict)
dict_.get(33, "default_value")
print(dict_.get(33) is None)

# accessing non-existend dict value via subindexing: throws KeyError
try:
    dict_[33]
except KeyError:
    print(f"Error {KeyError.__name__} caught")

try:
    del dict_[33]
except KeyError:
    print(f"Caught {KeyError.__name__}")

dict_.setdefault(44, "aąsdf")
dict_.pop(100)

# dictionary's pop has to receive a key!!!
dict_.pop(1)

dict_.popitem()


x = 123
bin(x).strip("0b")
oct(x)
