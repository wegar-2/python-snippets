

class MyMetaclass(type):
    def __new__(mcs, name, bases, class_dict):
        cls_ = super().__new__(mcs, name, bases, class_dict)
        cls_.special_member = "_____SPECIAL_MEMBER_____"
        return cls_


class MyClass(metaclass=MyMetaclass):
    def __init__(self):
        self.my_member = [123, 333]


class AnotherMetaclass(type):
    def __new__(mcs, *args, **kwargs):
        cls_ = super().__new__(mcs, *args, **kwargs)
        cls_.very_special_member = "VERY_SPECIAL_MEMBER"
        return cls_


class AnotherClass(metaclass=AnotherMetaclass):
    def __init__(self):
        self.ordinary_member = "ordinary member!"


if __name__ == "__main__":

    obj = MyClass()
    print(obj.special_member)

    another_obj = AnotherClass()
    print(another_obj.ordinary_member)
    print(another_obj.very_special_member)


# REFERENCES:
#   1) https://realpython.com/python-metaclasses/#custom-metaclasses
#   2) https://sentry.io/answers/what-are-Python-metaclasses/
#   3) https://www.datacamp.com/tutorial/python-metaclasses
#   4) https://profil-software.com/blog/development/demystifying-python-metaclasses-why-are-they-so-special/
#   5) https://www.pythontutorial.net/python-oop/python-metaclass/
#   6) https://www.pythontutorial.net/python-oop/python-metaclass-example/
