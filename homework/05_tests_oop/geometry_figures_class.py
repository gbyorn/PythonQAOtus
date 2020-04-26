import math


class GeometryFigure:
    def __init__(self, *args):
        self.sides = [*args]

    def name(self):
        pass

    def area(self):
        pass

    def angles(self):
        pass

    def perimeter(self):
        pass

    def add_square(self, second_figure):
        pass


class Circle(GeometryFigure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 1:
            print("Error! Incorrect count sides.")
            return None
        else:
            return super().__new__(cls)

    def area(self):
        return (self.sides[0] ** 2) * math.pi

    def perimeter(self):
        return self.sides[0] * 2 * math.pi


class Triangle(GeometryFigure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 3:
            print("Error! Incorrect count sides.")
            return None
        if (args[0] + args[1]) <= args[2] or (args[0] + args[2]) <= args[1] or (args[1] + args[2] <= args[0]):
            print("Error! Incorrect length sides.")
        else:
            return super().__new__(cls)

    def area(self):
        p = (sum(self.sides) / 2)
        first_side = self.sides[0]
        second_side = self.sides[1]
        third_side = self.sides[2]
        return math.sqrt(p * (p - first_side) * (p - second_side) * (p - third_side))

    def perimeter(self):
        return sum(self.sides)


class Rectangle(GeometryFigure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 2:
            print("Error! Incorrect count sides.")
            return None
        else:
            return super().__new__(cls)

    def area(self):
        return self.sides[0] * self.sides[1]

    def perimeter(self):
        return sum(self.sides) * 2


class Square(GeometryFigure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 1:
            print("Error! Incorrect count sides.")
            return None
        else:
            return super().__new__(cls)

    def area(self):
        return self.sides[0] ** 2

    def perimeter(self):
        return self.sides[0] * 4


circle = Circle(7)
triangle = Triangle(2, 2, 3)
rectangle = Rectangle(2, 4)
square = Square(4)
print(triangle.perimeter())
print(circle.perimeter())
print(rectangle.perimeter())
print(square.perimeter())
