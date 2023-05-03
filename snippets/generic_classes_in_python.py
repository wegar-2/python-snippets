from typing import Generic, TypeVar, get_args

# TypeVar T is allowed to be only either an integer or a float
T = TypeVar("T", int, float)


class Generic2dPoint(Generic[T]):

    def __init__(self, x: T, y: T):
        self.coord_x: T = x
        self.coord_y: T = y

    def __str__(self):
        return f"Point in 2d with coordinates x={self.coord_x}, y={self.coord_y} and member type of class " \
               f"{self.coord_x.__class__.__name__}"


if __name__ == "__main__":

    # case 1: point with integer coordinates
    point_int = Generic2dPoint[int](x=12, y=33)
    print(point_int)

    # case 2: point with float coordinates
    point_float = Generic2dPoint[float](x=3.22, y=-123.33)
    print(point_float)
