class TestDict:
    def test_dict_type(self, fixture_dict_params):
        assert isinstance(fixture_dict_params, dict)

    def test_dict_one(self, fixture_dict_params):
        assert fixture_dict_params.get('31') == 1

    def test_dict_two(self, fixture_dict_params):
        dict_copy = fixture_dict_params.copy()
        assert dict_copy == fixture_dict_params

    def test_dict_three(self, fixture_dict_params):
        copy_of_dict = fixture_dict_params.copy()
        copy_of_dict.pop('32')
        assert copy_of_dict == {'31': 1, '33': 3, '34': 4, '35': 5}

    def test_dict_four(self, fixture_dict_params):
        copy_of_dict = fixture_dict_params.copy()
        copy_of_dict.clear()
        assert copy_of_dict == {}

    def test_dict_five(self, fixture_dict_params):
        copy_of_dict = fixture_dict_params.copy()
        copy_of_dict.update({'36': 6})
        assert copy_of_dict == {'31': 1, '32': 2, '33': 3, '34': 4, '35': 5, '36': 6}
