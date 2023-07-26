

class Point2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(self.__dict__.keys())

    def __setattr__(self, key, value):
        pass

    def __getattr__(self, item):
        pass


point = Point2d(10, 22)
print(point.__dict__.keys())
