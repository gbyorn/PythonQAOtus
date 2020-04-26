import geometry_figures_class as figure
import math


class TestCircle:
    def test_name(self, fixture_circle_params):
        pass

    def test_area(self, fixture_circle_params):
        circle = figure.Circle(fixture_circle_params)
        area = (fixture_circle_params ** 2) * math.pi
        assert circle.area() == area

    def test_angles(self, fixture_circle_params):
        pass

    def test_perimeter(self, fixture_circle_params):
        circle = figure.Circle(fixture_circle_params)
        perimeter = 2 * math.pi * fixture_circle_params
        assert circle.perimeter() == perimeter

    def test_add_square(self, fixture_circle_params):
        pass
