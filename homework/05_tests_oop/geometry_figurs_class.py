class GeometryFigure:
    def name(self):
        pass

    def area(self):
        pass

    def angles(self):
        pass

    def perimeter(self):
        pass

    def add_square(self):
        pass


class Circle(GeometryFigure):
    def __init__(self, length):
        self.length = length


class Triangle(GeometryFigure):
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side


class Rectangle(GeometryFigure):
    def __init__(self, short_side, long_side):
        self.short_side = short_side
        self.long_side = long_side


class Square(GeometryFigure):
    def __init__(self, side):
        self.side = side
