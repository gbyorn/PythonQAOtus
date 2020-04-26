import geometry_figures_class as figure
import math


class TestTriangle:
    def test_name(self, fixture_triangle_params):
        pass

    def test_area(self, fixture_triangle_params):
        triangle = figure.Triangle(*fixture_triangle_params)
        first_side = fixture_triangle_params[0]
        second_side = fixture_triangle_params[1]
        third_side = fixture_triangle_params[2]
        p = (first_side + second_side + third_side) / 2
        area = math.sqrt(p * (p - first_side) * (p - second_side) * (p - third_side))
        assert triangle.area() == area

    def test_angles(self, fixture_triangle_params):
        pass

    def test_perimeter(self, fixture_triangle_params):
        triangle = figure.Triangle(*fixture_triangle_params)
        perimeter = sum(fixture_triangle_params)
        assert triangle.perimeter() == perimeter

    def test_add_square(self, fixture_triangle_params):
        pass
