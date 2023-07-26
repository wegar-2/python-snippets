# =====================================================================================================================
# (1) __new__
# (2) __init__
# (3) __hash__
# (4) __eq__
# (5) __iter__
# (6) __next__
# (7) __setattr__
# (8) __getattr__
# (9) __len__
# (10) __str__
# (11) __repr__
# =====================================================================================================================


# Point2d: __new__,  __init__, __eq__, __len__, __str__, __repr__
class Point2d:

    def __new__(cls, *args, **kwargs):
        print(f"Inside {cls.__new__.__name__} method")
        # NOTE: object.__new__() takes exactly one argument (the type to instantiate):
        obj = super().__new__(cls)
        obj.x = obj.y = None
        return obj

    def __init__(self, x, y):
        print(f"Inside {self.__init__.__name__} method")
        self.x = x
        self.y = y

    def __str__(self):
        """ provides the informal string representation of an object, aimed at the user """
        return f"Point2d({self.x}, {self.y})"

    def __repr__(self):
        """ provides the official string representation of an object, aimed at the programmer """
        return f"Point2d({self.x}, {self.y})"


def main():
    point = Point2d(123, 33)
    print(point)


if __name__ == "__main__":
    main()

