from enum import Enum, auto


class CarColor(Enum):
    BLACK = auto
    RED = auto
    WHITE = auto


class CarBodyStyle(Enum):
    SEDAN = auto
    HATCHBACK = auto
    MINIVAN = auto
    ROADSTER = auto


class CarMetaclass(type):
    """
    This metaclass is used just for fun & practice, it contributes nothing to the example with regard to
    demonstrating of how enumerations work.
    """
    def __new__(mcs, *args, **kwargs):
        inst = super().__new__(mcs, *args, **kwargs)
        inst.body_style = None
        inst.car_color = None
        return inst


class Car(metaclass=CarMetaclass):
    """
    """

    counter = 0

    def __init__(self, body_style: CarBodyStyle, car_color: CarColor):

        self.body_style = body_style
        self.car_color = car_color

        self.__class__.counter += 1
        self.id = self.__class__.counter

    def __repr__(self):
        return f"This car has id {self.id}, body style: {self.body_style} and is of color {self.car_color}"


if __name__ == "__main__":

    red_sedan = Car(body_style=CarBodyStyle.SEDAN, car_color=CarColor.RED)
    black_roadster = Car(body_style=CarBodyStyle.ROADSTER, car_color=CarColor.BLACK)

    print(f"Red sedan: {red_sedan}")
    print(f"Black roadster: {black_roadster}")


# References:
#   1) https://realpython.com/python-enum/#using-enumerations-two-practical-examples
