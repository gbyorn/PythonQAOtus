class TestString:
    def test_dict_type(self, fixture_string_params):
        assert isinstance(fixture_string_params, str)
