class TestList:
    def test_list_type(self, fixture_list_params):
        assert isinstance(fixture_list_params, list)

    def test_list_one(self, fixture_list_params):
        list_copy = fixture_list_params.copy()
        assert list_copy == fixture_list_params

    def test_list_two(self, fixture_list_params):
        list_copy = fixture_list_params.copy()
        list_copy.reverse()
        assert list_copy == [15, 14, 13, 12, 11]

    def test_list_three(self, fixture_list_params):
        list_copy = fixture_list_params.copy()
        list_copy.clear()
        assert list_copy == []

    def test_list_four(self, fixture_list_params):
        list_copy = fixture_list_params.copy()
        list_copy.append(16)
        assert list_copy == [11, 12, 13, 14, 15, 16]

    def test_list_five(self, fixture_list_params):
        list_copy = fixture_list_params.copy()
        list_copy.remove(13)
        assert list_copy == [11, 12, 14, 15]

