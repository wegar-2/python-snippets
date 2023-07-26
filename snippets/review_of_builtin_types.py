from collections import deque


# =====================================================================================================================
# ================================================ LISTS ==============================================================
# =====================================================================================================================
list_ = [1, "a", "b", "qwerty", 32]
# (1) .pop() method
print(list_.pop())
print(list_.pop(0))
print(list_)
# (2) .append() method
list_.append(903)
list_.append("zxcv")
print(list_)
# (3) access out of bound index using indexing
try:
    list_[10]
except IndexError:
    print(f"{IndexError.__name__} caught when accessing out of bound list element")
# (4) pop out of bound index: also error
try:
    list_.pop(10)
except IndexError:
    print(f"{IndexError.__name__} caught when popping out of bound list element")
# (5) .extend() method
list_.extend([1, 2, 3])
print(list_)
# (6) .__add__() vs .extend() for lists
list_.extend([4, 5])
print(list_) # extend(): works in place
list_ = list_ + [6, 7, 1, 2, 3]
print(list_) # __add__(): returns extended list, has to be assigned
# (7) find first occurrence of given element in a list
print(list_[list_.index(903)])
# (8) find all occurrences of given element in a list
print([key_ for key_, val_ in enumerate(list_) if val_ == 1])
# (9) reverse() the order of list
print(list_)
list_.reverse()
print(list_)
# (10) .insert() into the list
list_.insert(3, 0)
print(list_)
# (11) .remove() method
list_.remove(1)
print(list_)
# (12) remove all occurrences of integer 2
list_ = [el for el in list_ if el != 2]
print(list_)
# =====================================================================================================================


# =====================================================================================================================
# ============================================= DICTIONARY ============================================================
# =====================================================================================================================
dict_ = {"a": 123, "b": 90}
print(dict_)
# (1) .update()
dict_.update({"c": 876})
print(dict_)
# (2) .get(, [default])
print(dict_.get("a"))
print(dict_.get("z", "NA!"))
print(dict_.get("z") is None)
try:
    dict_["z"]
except KeyError:
    print(f"Caught {KeyError.__name__} when trying to access")
# Note: difference between get() called with key only (no default) and subindexing a dictionary
# (3) .pop():
dict_.update({"q": 9, "t": 3})
print(dict_)
print(dict_.pop("a"))
print(dict_)
# (4) merge two dictionaries: UNION OPERATOR
dict_new = {"k": 9, "l": 44}
print(dict_new)
dict_ = dict_ | dict_new
print(dict_)
# (5) merge two dictionaries: UNPACKING
dict_new = {"m": 11, "n": 434}
print(dict_new)
dict_ = {**dict_, **dict_new}
print(dict_)
# (7) .popitem()
print(dict_)
print(dict_.popitem()) # NOTE: .popitem() returns a tuple!!!
print(dict_)
# (6) .setdefault()
print(dict_.setdefault("z", "ZVALUE"))
print(dict_)
# =====================================================================================================================


# =====================================================================================================================
# ============================================= SETS ==================================================================
# =====================================================================================================================
set_ = {0, 1, 2}
# (1) .add(), .update()
set_.add(3)
print(set_)
set_.update({9, 10})
print(set_)
# (2) .union()
set_ = set_.union({4, 5})
print(set_)
# (3) .intersection()
print(set_.intersection({1, 2, 3}))
# (4) .difference()
print(set_.difference({0, 1, 2, 3, 4}))
# (5) .intersection_update()
set1 = {0, 1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
set1.intersection_update(set2) # take the intersection and assign it to set1
print(set1)
print(set2)
# (6) .difference_update()
set1 = {0, 1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
set1.difference_update(set2) # take the difference set1 - set2 and assign it to set1
print(set1)
print(set2)
# (7) .pop() vs .discard() vs .remove()
print(set_)
set_.pop()
print(set_)
set_.remove(10)
print(set_)
try:
    set_.remove(10)
except KeyError:
    print(f"Caught {KeyError.__class__} in call to remove() on a set")
set_.discard(9)
print(set_)
set_.discard(9) # no error!
# =====================================================================================================================


# =====================================================================================================================
# =========================================== collections.deque =======================================================
# =====================================================================================================================
deque_ = deque(range(10))
print(deque_)
# (1) .append(), appendleft()
deque_.append(1000)
deque_.appendleft(-1000)
print(deque_)
# (2) .pop(), .popleft()
print(deque_.pop())
print(deque_.popleft())
print(deque_)
# (3) .reverse()
deque_.reverse()
print(deque_)
# (4) .extend(), .extendleft()
deque_.extend([1000, 1001])
deque_.extendleft([-2000, -1000])
print(deque_)
# (5) .insert()
deque_.insert(3, 1000)
# (6) .remove()
deque_.remove(-2000)
print(deque_)
# (7) .count()
print(deque_)
print(deque_.count(1000))
# =====================================================================================================================

# =====================================================================================================================
# ================================================ BYTES ==============================================================
# =====================================================================================================================

# =====================================================================================================================


# =====================================================================================================================
# ================================================ FROZENSET ==========================================================
# =====================================================================================================================
# =====================================================================================================================


# =====================================================================================================================
# ================================================ BYTEARRAY ==========================================================
# =====================================================================================================================
# =====================================================================================================================
