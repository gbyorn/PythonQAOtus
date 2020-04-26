import geometry_figures_class as figure
import math


class TestRectangle:
    def test_name(self, fixture_rectangle_params):
        pass

    def test_area(self, fixture_rectangle_params):
        rectangle = figure.Rectangle(*fixture_rectangle_params)
        area = fixture_rectangle_params[0] * fixture_rectangle_params[1]
        assert rectangle.area() == area

    def test_angles(self, fixture_rectangle_params):
        pass

    def test_perimeter(self, fixture_rectangle_params):
        rectangle = figure.Rectangle(*fixture_rectangle_params)
        perimeter = sum(fixture_rectangle_params) * 2
        assert rectangle.perimeter() == perimeter

    def test_add_square(self, fixture_rectangle_params):
        pass
