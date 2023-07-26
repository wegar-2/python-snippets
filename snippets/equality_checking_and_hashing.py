import typing as t


class Point2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Point2d(x=1, y=3)
point2 = Point2d(x=1, y=3)
print(point1 is point2)
print(point1 == point2)


class BetterPoint2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


bpoint1 = BetterPoint2d(1, 3)
bpoint2 = BetterPoint2d(1, 3)

print(bpoint1 is bpoint2) # False
print(bpoint1 == bpoint2) # True


str1 = "hello world"
print(hash(str1))


# =====================================================================================================================
class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.a == other.a

    def __hash__(self):
        return self.a


a = Example(1, 2)
b = Example(1, 3)
c = Example(1, 11)
d = Example(1, 10)

for obj_ in [a, b, c, d]:
    print(hash(obj_))

obj = {a: 5, b: 10, c: 11, d: 10}
# what will this print?
print(obj[a])


list1 = [1, 2, 3]
list2 = list1

print(id(list1))
print(id(list2))
list1.append(4)
print(id(list1))
print(id(list2))

