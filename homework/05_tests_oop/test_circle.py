import geometry_figures_class as figure
import math


class TestCircle:
    def test_name(self, fixture_circle_params):
        circle = figure.Circle(fixture_circle_params)
        name = "Geometry figure Circle"
        assert circle.name() == name

    def test_area(self, fixture_circle_params):
        circle = figure.Circle(fixture_circle_params)
        area = (fixture_circle_params ** 2) * math.pi
        assert circle.area() == area

    def test_angles(self, fixture_circle_params):
        circle = figure.Circle(fixture_circle_params)
        angles = 0
        assert circle.angles() == angles

    def test_perimeter(self, fixture_circle_params):
        circle = figure.Circle(fixture_circle_params)
        perimeter = 2 * math.pi * fixture_circle_params
        assert circle.perimeter() == perimeter

    def test_add_square(self, fixture_circle_params):
        another_rectangle = figure.Rectangle(2, 5)
        circle = figure.Circle(fixture_circle_params)
        add_area = another_rectangle.area() + circle.area()
        assert circle.add_square(another_rectangle) == add_area
