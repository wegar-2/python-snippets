import pandas as pd


class MyClass:

    def __new__(cls, *args, **kwargs):
        print(f"Inside {cls.__new__.__name__} method call of {cls.__name__} class! ")

    def __init__(self):
        print(f"Inside {self.__init__.__name__} method call of {self.__class__.__name__} class! ")


class NicerClass:

    def __new__(cls, *args, **kwargs):
        print(f"Inside {cls.__new__.__name__} method call of {cls.__name__} class! ")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print(f"Inside {self.__init__.__name__} method call of {self.__class__.__name__} class! ")


class AnotherClass:

    def __new__(cls, *args, **kwargs):
        print(f"Inside {cls.__new__.__name__} method call of {cls.__name__} class! ")
        inst = object.__new__(cls)
        return inst

    def __init__(self):
        print(f"Inside {self.__init__.__name__} method call of {self.__class__.__name__} class! ")
        self.df = pd.DataFrame(data={"a": [1, 2, 3]})


if __name__ == "__main__":

    # Case 1: __new__ method of MyClass does not return anything; hence, only __new__ gets called
    obj1 = MyClass()

    # Case 2: class NicerClass returns from __new__: the returned object is obtained via call to super()'s
    # __new__ method
    obj2 = NicerClass()

    # Case 3: class AntoherClass inherits from object; object's __new__ is called inside AnotherClass' __new__
    print(f"Inheritance message for class {AnotherClass.__name__}: {AnotherClass.__bases__}")
    obj3 = AnotherClass()


# References:
#   1) https://www.pythontutorial.net/python-oop/python-__new__/
#   2) https://realpython.com/python-class-constructor/
