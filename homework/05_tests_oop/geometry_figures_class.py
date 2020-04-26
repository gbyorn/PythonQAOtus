import math


class GeometryFigure:
    def __init__(self, *args):
        self.sides = [*args]

    def name(self):
        return 'Geometry figure'

    def area(self):
        return self.sides[0] * self.sides[1]

    def angles(self):
        return len(self.sides)

    def perimeter(self):
        return sum(self.sides)

    def add_square(self, second_figure):
        try:
            return self.area() + second_figure.area()
        except AttributeError:
            return "Error! Incorrect type of class."


class Circle(GeometryFigure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 1:
            print("Error! Incorrect count sides.")
            return None
        else:
            return super().__new__(cls)

    def name(self):
        return GeometryFigure.name(self) + ' Circle'

    def area(self):
        return (self.sides[0] ** 2) * math.pi

    def angles(self):
        return 0

    def perimeter(self):
        return GeometryFigure.perimeter(self) * 2 * math.pi


class Triangle(GeometryFigure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 3:
            print("Error! Incorrect count sides.")
            return None
        if (args[0] + args[1]) <= args[2] or (args[0] + args[2]) <= args[1] or (args[1] + args[2] <= args[0]):
            print("Error! Incorrect length sides.")
        else:
            return super().__new__(cls)

    def name(self):
        return GeometryFigure.name(self) + ' Triangle'

    def area(self):
        p = (sum(self.sides) / 2)
        first_side = self.sides[0]
        second_side = self.sides[1]
        third_side = self.sides[2]
        return math.sqrt(p * (p - first_side) * (p - second_side) * (p - third_side))

    def perimeter(self):
        return GeometryFigure.perimeter(self)


class Rectangle(GeometryFigure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 2:
            print("Error! Incorrect count sides.")
            return None
        else:
            return super().__new__(cls)

    def name(self):
        return GeometryFigure.name(self) + ' Rectangle'

    def angles(self):
        return GeometryFigure.angles(self) * 2

    def perimeter(self):
        return GeometryFigure.perimeter(self) * 2


class Square(GeometryFigure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 1:
            print("Error! Incorrect count sides.")
            return None
        else:
            return super().__new__(cls)

    def name(self):
        return GeometryFigure.name(self) + ' Square'

    def area(self):
        return self.sides[0] ** 2

    def angles(self):
        return GeometryFigure.angles(self) * 4

    def perimeter(self):
        return GeometryFigure.perimeter(self) * 4
