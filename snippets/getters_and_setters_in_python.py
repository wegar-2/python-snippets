

class Person:
    """
    This class represents a person that has a name and an age.
    """

    def __init__(
            self,
            name: str,
            age: int
    ):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        self._age = value

    def __repr__(self):
        return f"Person named {self._name} of age {self._age}"


class Point2d:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        self.__dict__[f"_{key}"] = value

    def __getattr__(self, item):
        return self.__dict__[f"_{item}"]

    def __repr__(self):
        return f"Point2d({self._x}, {self._y})"


if __name__ == "__main__":

    # Example 1: using class that makes use of properties
    person = Person(name="John", age=44)
    print(person)
    person.age = 33
    person.name = "Louis"
    print(person)

    # Example 2: using class that uses magic methods __setattr__ and __getattr__
    point = Point2d(1.33, -34.2)
    print(point)

    print(f"Members of the class {point.__class__.__name__} instance: ")
    for key, val in enumerate(dir(point)):
        print(f"Member #{key}: {val}")

    # Remark: note that neither x nor y is a mamber of instance point of class Point2d.
    # This is so because the function __setattr__ is defined and it is responsible for the assignments
    # that take place inside the call to __init__ of the class Point2d.

