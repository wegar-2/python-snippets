

l = [1, "a"]
print(l)

# 1. .append()
l.append(123.33)
# 2. .extend() --- works in place!
l.extend(["qwe", 5, 55])
# 3. pop without args
print(l)
print(l.pop())
print(l)
# 4. pop with arg -- pop specific list element
l.pop(2)
# 5. index --- find firs occurrence
l = [1, 2, 3, 5, 4, 2, 4, 1, 2]
print(l.index(4))
print(l[l.index(4)])
# 6. insert value
print(l)
l.insert(1, "newval")
print(l)
# 7. count number of occurrences of an element
l.count(4)
# 8. trying to access out of bound element raises IndexError
try:
    l[100]
except IndexError:
    print(f"Caught error {IndexError.__name__}")
# 9. remove() vs del
l = [1, 2, 3, 4]
l.remove(3)
print(l)
# note: attempt to delete an out-of-range element raises IndexError
try:
    del l[4]
except IndexError:
    print(f"Caught {IndexError.__name__} when trying to delete an out of range element")
# 10. reversing a list in place, reversed() method call
l = [1, 2, 3, 4, 5]
print(l)
l.reverse()
print(l)
print(list(reversed(l)))

