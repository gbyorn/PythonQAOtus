class TestString:
    def test_str_type(self, fixture_string_params):
        assert isinstance(fixture_string_params, str)

    def test_str_one(self, fixture_string_params):
        new_string = fixture_string_params.rstrip('5')
        assert new_string == '1234'

    def test_str_two(self, fixture_string_params):
        new_string = fixture_string_params.replace('3', '6')
        assert new_string == '12645'

    def test_str_three(self, fixture_string_params):
        assert fixture_string_params.find('4') == 3

    def test_str_four(self, fixture_string_params):
        assert fixture_string_params.startswith('1')

    def test_str_five(self, fixture_string_params):
        assert fixture_string_params.isalnum()

