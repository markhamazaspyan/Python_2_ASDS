from abc import ABCMeta, abstractmethod
import time
import copy

"""
Use prototype design pattern and classes of your choice. create an abstract class Shape and
concrete classes extending the Shape class: Circle, Square and Rectangle. Define a class
ShapeCache which stores shape objects in a dictionary and returns their clones when
requested. Create some objects and do some operations to test your classes.
"""


class Shape(metaclass=ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def describe(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


class Circle(Shape):
    def __init__(self, name):
        super().__init__()
        time.sleep(3)
        self.name = name
        self.type = "Circle"

    def describe(self):
        print(f"Object is a {self.name} {self.type}")


class Square(Shape):
    def __init__(self, name):
        super().__init__()
        time.sleep(3)
        self.name = name
        self.type = "Square"

    def describe(self):
        print(f"Object is a {self.name} {self.type}")


class Rectangle(Shape):
    def __init__(self, name):
        super().__init__()
        time.sleep(3)
        self.name = name
        self.type = "Rectangle"

    def describe(self):
        print(f"Object is a {self.name} {self.type}")


class ShapeCache:

    cache = {}

    @staticmethod
    def get_shape(cid):
        SHAPE = ShapeCache.cache.get(cid, None)
        return SHAPE.clone()

    @staticmethod
    def load():
        circle = Circle('Black')
        circle.set_id("1")
        ShapeCache.cache[circle.get_id()] = circle

        rec = Rectangle('Black')
        rec.set_id("2")
        ShapeCache.cache[rec.get_id()] = rec

        square = Square('Black')
        square.set_id("3")
        ShapeCache.cache[square.get_id()] = square

if __name__ == '__main__':
    ShapeCache.load()

    obj1 = ShapeCache.get_shape("1")
    print(obj1.get_type())
    obj1.describe()
    print("\n")

    obj2 = ShapeCache.get_shape("2")
    print(obj2.get_type())
    obj2.describe()
    print("\n")

    obj3 = ShapeCache.get_shape("3")
    print(obj3.get_type())
    obj3.describe()
    print("\n")

    obj4 = ShapeCache.get_shape("1")
    obj4.name = "Red"
    print(obj4.get_type())
    obj4.describe()
