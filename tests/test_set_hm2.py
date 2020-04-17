class TestSet:
    def test_set_type(self, fixture_set_params):
        assert isinstance(fixture_set_params, set)

    def test_set_one(self, fixture_set_params):
        set_copy = fixture_set_params.copy()
        assert set_copy == fixture_set_params

    def test_set_two(self, fixture_set_params):
        set_copy = fixture_set_params.copy()
        assert set_copy.union({26, 27, 28}) == {21, 22, 23, 24, 25, 26, 27, 28}

    def test_set_three(self, fixture_set_params):
        set_copy = fixture_set_params.copy()
        assert set_copy.intersection({21, 23, 26, 27}) == {21, 23}

    def test_set_four(self, fixture_set_params):
        set_copy = fixture_set_params.copy()
        assert set_copy.difference({21, 23, 26, 27}) == {22, 24, 25}

    def test_set_five(self, fixture_set_params):
        set_copy = fixture_set_params.copy()
        assert set_copy.symmetric_difference({21, 23, 26, 27}) == {22, 24, 25, 26, 27}

