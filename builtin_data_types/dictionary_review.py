from string import ascii_letters

d = {1: "q", 2: "b"}

# 1. .update() - add new entries; in case of collision: overwrites
d.update({3: "e"})
d.update({3: "qwerty"})
# 2. pop() - in case of dict it HAST TO get an arg
print(d.pop(3))
print(d)
# 3. accessors
# 3.1. getitem()
d = dict(zip(range(10), ascii_letters[:10]))
try:
    d[10]
except KeyError:
    print("Caught KeyError when trying to access non existent dict entry")
# 3.2. .get method
print(d.get(10) is None)
# 3.3.
d.setdefault(10, "qwerty")

del d[10]
# 3.3. .pop() with no args equivalent for dicts: .popitem()
d.popitem()

# 4. get iterable with 2-tuple of key-value pairs
d.items()
d.setdefault(10, "qwerty")




dict_ = {1: "qwerty"}
dict_.update({2: "qwe"})
del dict_[2]

del dict_[2]
dict_[2]
