import geometry_figures_class as figure


class TestSquare:
    def test_name(self, fixture_square_params):
        square = figure.Square(fixture_square_params)
        name = "Geometry figure Square"
        assert square.name() == name

    def test_area(self, fixture_square_params):
        square = figure.Square(fixture_square_params)
        area = fixture_square_params ** 2
        assert square.area() == area

    def test_angles(self, fixture_square_params):
        square = figure.Square(fixture_square_params)
        angles = 4
        assert square.angles() == angles

    def test_perimeter(self, fixture_square_params):
        square = figure.Square(fixture_square_params)
        perimeter = fixture_square_params * 4
        assert square.perimeter() == perimeter

    def test_add_square(self, fixture_square_params):
        another_rectangle = figure.Rectangle(2, 5)
        square = figure.Square(fixture_square_params)
        add_area = another_rectangle.area() + square.area()
        assert square.add_square(another_rectangle) == add_area
